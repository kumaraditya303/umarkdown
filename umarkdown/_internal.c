#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <cmark.h>
/**
 * Documentation for Ultra Markdown.
 */
PyDoc_STRVAR(_internal_markdown_doc, "Converts Markdown to HTML\n \
 \
 Set source_pos=True to include source position attribute.\n \
 Set hard_breaks=True to treat newlines as hard line breaks.\n \
 Set no_breaks=True to render soft line breaks as spaces.\n \
 Set unsafe=True to render raw HTML and dangerous URLs.\n \
 Set smart=True to use smart punctuation.\n \
 Set validate_utf8=True to replace invalid UTF-8 sequences with U+FFFD. \
");

PyDoc_STRVAR(_internal_doc, "Ultra Markdown is an ultrafast Markdown parser written in\
pure C with bindings for Python3.7+. It internally uses CMark,\
an ultrafast C library for parsing Markdown to HTML.\
Unlike others, Ultra Markdown is written using Python's C API\
which makes it ultrafast for parsing Markdown.");

/**
 * Implements markdown to html conversion.
 */

static PyObject *markdown(PyObject *self, PyObject *args, PyObject *kwargs)
{
    int options = CMARK_OPT_DEFAULT;
    char *kwlist[] = {"text", "text_file", "output_file", "source_pos", "hard_breaks",
                      "no_breaks", "smart", "unsafe", "validate_utf8", NULL};
    char *text = NULL;
    char *text_file = NULL;
    char *output_file = NULL;
    PyObject *osourcepos = NULL;
    PyObject *ohardbreaks = NULL;
    PyObject *onobreaks = NULL;
    PyObject *osmart = NULL;
    PyObject *ounsafe = NULL;
    PyObject *ovalidateutf8 = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "|sssOOOOOO", kwlist, &text, &text_file,
                                     &output_file, &osourcepos, &ohardbreaks, &onobreaks,
                                     &osmart, &ounsafe, &ovalidateutf8))
    {
        return NULL;
    }
    if ((text == NULL && text_file == NULL) || (text != NULL && text_file != NULL))
    {
        PyErr_SetString(PyExc_TypeError, "either provide text or text_file");
        return NULL;
    }

    if (osourcepos != NULL && PyObject_IsTrue(osourcepos))
    {
        options |= CMARK_OPT_SOURCEPOS;
    }
    if (ohardbreaks != NULL && PyObject_IsTrue(ohardbreaks))
    {
        options |= CMARK_OPT_HARDBREAKS;
    }
    if (onobreaks != NULL && PyObject_IsTrue(onobreaks))
    {
        options |= CMARK_OPT_NOBREAKS;
    }
    if (osmart != NULL && PyObject_IsTrue(osmart))
    {
        options |= CMARK_OPT_SMART;
    }
    if (ounsafe != NULL && PyObject_IsTrue(ounsafe))
    {
        options |= CMARK_OPT_UNSAFE;
    }
    if (ovalidateutf8 != NULL && PyObject_IsTrue(ovalidateutf8))
    {
        options |= CMARK_OPT_VALIDATE_UTF8;
    }
    if (text_file != NULL)
    {
        FILE *fin;
        fin = fopen(text_file, "r");
        if (fin == NULL)
        {
            PyErr_SetString(PyExc_ValueError, "file not found");
            return NULL;
        }

        cmark_node *doc = cmark_parse_file(fin, options);
        fclose(fin);
        char *result = cmark_render_html(doc, options);
        cmark_node_free(doc);
        if (output_file != NULL)
        {
            FILE *fout;
            fout = fopen(output_file, "w+");
            fprintf(fout, "%s", result);
            fclose(fout);
            if (PyErr_Occurred())
            {
                return NULL;
            }
            Py_RETURN_TRUE;
        }
        return Py_BuildValue("s", result);
    }

    char *result = cmark_markdown_to_html(text, strlen(text), options);
    return Py_BuildValue("s", result);
}

/*
 * Module Methods Definition.
 */

static PyMethodDef methods[] = {
    {"markdown", (PyCFunction)markdown, METH_VARARGS | METH_KEYWORDS, _internal_markdown_doc},
    {NULL, NULL, 0, NULL}};

/*
 * Module Definition.
 */

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "_internal",
    _internal_doc,
    -1,
    methods};

/*
 * Module Initialization.
 */
PyMODINIT_FUNC PyInit__internal(void)
{
    return PyModule_Create(&module);
}
