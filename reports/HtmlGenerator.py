

from core.Core import Core
from objects.CssAttribute import CssAttribute, CssAttributeType
from objects.HtmlAttribute import HtmlAttributeType
from objects.HtmlElement import HtmlElement
from objects.HtmlElementType import HtmlElementType


class HtmlGenerator():

    def __init__(self, fileName="proyecto"):
        self.htmlStr = ""
        self.cssStr = ""
        self.filename = fileName
        self._generateHtml()
        self._generateCss()
        self._generateFiles()
        print('Reporte generado con exito')

    def _createFile(self, content, filename):
        try:
            with open(f'docs/{filename}', 'w') as f:
                f.write(content)
        except FileNotFoundError:
            with open(f'docs/{filename}', 'x') as f:
                f.write(content)

    def _generateFiles(self):
        # html
        self._createFile(self.htmlStr, self.filename+".html")
        # css
        self._createFile(self.cssStr, self.filename+".css")

    def _generateCss(self):
        self.cssStr = ""
        for i in range(1, len(Core.SymbolTable)):
            self.cssStr += self._generateElementStyle(Core.SymbolTable[i])

    def _generateElementStyle(self, element: HtmlElement):

        props = ""
        for style in element.styles:

            if style.type == CssAttributeType.ALIGNMENT:

                aligment = "left"

                if style.value == "Centro":
                    aligment = "center"
                elif style.value == "Derecha":
                    aligment = "right"

                props += f"text-align: {aligment};\n"

            if style.type == CssAttributeType.BACKGROUNG_COLOR:
                color = style.value
                props += f"background-color: rgba({color[0]},{color[1]},{color[2]});\n"

            if style.type == CssAttributeType.COLOR:
                color = style.value
                props += f"size: 12px;\n"
                props += f"color: rgba({color[0]},{color[1]},{color[2]});\n"

            if style.type == CssAttributeType.HEIGHT:
                props += f"height: {style.value}px;\n"

            if style.type == CssAttributeType.WIDHT:
                props += f"width: {style.value}px;\n"

            if style.type == CssAttributeType.POSITION:
                coords = style.value

                props += f"position: absolute;\n"
                props += f"left: {coords[0]}px;\n"
                props += f"top: {coords[1]}px;\n"

        return f"#{element.id}" + "{\n" + props + "}\n\n"

    def _generateHtml(self):

        self.htmlStr = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Proyecto Final LFP</title>
    <link rel="stylesheet" href="./{self.filename}.css">
</head>
    {self._generateHtmlElements()}
</html>
"""

    def _generateHtmlElements(self):
        root = Core.SymbolTable[0]
        return self._generateElement(root)

    def _generateElement(self, element: HtmlElement):

        childrenStr = ""
        for child in element.children:
            childrenStr += "\n\t"+self._generateElement(child)

        if element.tag == HtmlElementType.BODY:
            return f"<body>{childrenStr}</body>"

        if element.tag == HtmlElementType.LABEL:
            text = element.getAttribute(HtmlAttributeType.TEXT) or ""
            return f"<label id='{element.id}' >{text}{childrenStr}</label>"

        if element.tag == HtmlElementType.BUTTON:
            value = element.getAttribute(HtmlAttributeType.TEXT) or ""
            return f"<input id='{element.id}' type='submit' value='{value}' />"

        if element.tag == HtmlElementType.CHECKBOX:
            isChecked = element.getAttribute(HtmlAttributeType.IS_CHECKED) or ""

            checked = ""
            if isChecked:
                checked = "checked"

            return f"<input id='{element.id}' type='checkbox' value='{value}' {checked}/>"

        if element.tag == HtmlElementType.RADIOBUTTON:
            group = element.getAttribute(HtmlAttributeType.GROUP) or ""
            isChecked = element.getAttribute(HtmlAttributeType.IS_CHECKED) or ""

            checked = ""
            if isChecked:
                checked = "checked"

            return f"<input id='{element.id}' type='radio' name='{group}' {checked} />"

        if element.tag == HtmlElementType.TEXTAREA:
            value = element.getAttribute(HtmlAttributeType.VALUE) or ""
            return f"<textarea id={element.id}>{value}</textarea>"

        if element.tag == HtmlElementType.PASSWORD:
            value = element.getAttribute(HtmlAttributeType.TEXT) or ""
            return f"<input id='{element.id}' type='password' value='{value}' />"

        if element.tag == HtmlElementType.DIV:
            return f"<div id='{element.id}'>{childrenStr}</div>"

        if element.tag == HtmlElementType.TEXT:
            text = element.getAttribute(HtmlAttributeType.TEXT) or ""
            return f"<input id='{element.id}' type='text' value='{text}' />"

        print('unexpected element')
