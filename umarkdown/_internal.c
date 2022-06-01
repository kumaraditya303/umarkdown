#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <cmark.h>

PyDoc_STRVAR(_internal_markdown_doc, "Converts Markdown to HTML\n \
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

static PyObject *
markdown(PyObject *self, PyObject *args, PyObject *kwargs)
{
    int options = CMARK_OPT_DEFAULT;
    static char *kwlist[] = {"text", "text_file", "output_file", "source_pos", "hard_breaks",
                      "no_breaks", "smart", "unsafe", "validate_utf8", NULL};
    char *text = NULL;
    char *text_file = NULL;
    char *output_file = NULL;
    char *result = NULL;
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
        PyErr_SetString(PyExc_ValueError, "either provide text or text_file");
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
            PyErr_SetString(PyExc_FileNotFoundError, "file not found");
            return NULL;
        }
        Py_BEGIN_ALLOW_THREADS
        cmark_node *doc = cmark_parse_file(fin, options);
        fclose(fin);
        result = cmark_render_html(doc, options);
        cmark_node_free(doc);
        Py_END_ALLOW_THREADS
        goto write_output;
    }
    result = cmark_markdown_to_html(text, strlen(text), options);

write_output:
    if (output_file != NULL)
    {
        Py_BEGIN_ALLOW_THREADS
        FILE *fout = fopen(output_file, "w+");
        fputs(result, fout);
        fclose(fout);
        Py_END_ALLOW_THREADS
        Py_RETURN_TRUE;
    }

    return PyUnicode_FromString(result);
}

static PyMethodDef
mod_methods[] = {
    {"markdown", (PyCFunction)markdown, METH_VARARGS | METH_KEYWORDS, _internal_markdown_doc},
    {NULL, NULL, 0, NULL}
};

static int
mod_exec(PyObject *module)
{
    if (PyModule_AddStringConstant(module, "CMARK_VERSION", CMARK_VERSION_STRING) < 0){
        return -1;
    }
    return 0;
}

static PyModuleDef_Slot
mod_slots[] = {
    {Py_mod_exec, mod_exec},
    {0, NULL}
};

static struct
PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "_internal",
    .m_doc = _internal_doc,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
};

PyMODINIT_FUNC
PyInit__internal(void)
{
    return PyModuleDef_Init(&module);
}
