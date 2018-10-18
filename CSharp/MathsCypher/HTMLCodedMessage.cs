using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Web.UI;
using System.IO;
using System.Linq;

namespace MathsCypher
{
    internal class HTMLCodedMessage
    {
        private CodedMessage _codedMessage;
        private Dictionary<char, int> _mappings;
        private Random _random;

        public HTMLCodedMessage(CodedMessage codedMessage, Random random, Dictionary<char, int> mappings)
        {
            _codedMessage = codedMessage;
            _random = random;
            _mappings = mappings;
        }

        public void Generate(WebBrowser webBrowser)
        {
            using (var stringWriter = new StringWriter())
            using (var htmlWriter = new HtmlTextWriter(stringWriter))
            {
                htmlWriter.RenderBeginTag(HtmlTextWriterTag.Html);
                createHead(htmlWriter);
                createBody(htmlWriter);
                htmlWriter.RenderEndTag();

                writeHtmlToWebBrowser(webBrowser, stringWriter);
            }
        }

        private void createBody(HtmlTextWriter htmlWriter)
        {
            htmlWriter.RenderBeginTag(HtmlTextWriterTag.Body);
            createHeading(htmlWriter);
            createEncodedMessage(htmlWriter);
            createMappingsTable(htmlWriter);
            createCredits(htmlWriter);
            htmlWriter.RenderEndTag();
        }

        private void createCredits(HtmlTextWriter htmlWriter)
        {
            htmlWriter.AddAttribute(HtmlTextWriterAttribute.Class, "tiny");            
            htmlWriter.AppendText("All credit to Mrs Allan, quite possibly the best teacher in the whole world &#9786;", HtmlTextWriterTag.Div);
        }

        private void createMappingsTable(HtmlTextWriter htmlWriter)
        {
            htmlWriter.AppendText("Here's a clue!", HtmlTextWriterTag.P);
            
            htmlWriter.RenderBeginTag(HtmlTextWriterTag.Table);
            htmlWriter.RenderBeginTag(HtmlTextWriterTag.Tr);
            
            foreach (var mapping in _mappings)
            {
                createNewRowIfRequired(htmlWriter);
                htmlWriter.AppendText(string.Format("{0} = {1}", mapping.Value, mapping.Key), HtmlTextWriterTag.Td);
            }
            htmlWriter.RenderEndTag();
            htmlWriter.RenderEndTag();
        }

        private static int _columnIndex = 0;
        private static void createNewRowIfRequired(HtmlTextWriter htmlWriter)
        {
            if (_columnIndex % 6 == 0)
            {
                htmlWriter.RenderEndTag();
                htmlWriter.RenderBeginTag(HtmlTextWriterTag.Tr);
            }
            _columnIndex++;
        }

        private static void createHead(HtmlTextWriter htmlWriter)
        {
            htmlWriter.RenderBeginTag(HtmlTextWriterTag.Head);
            htmlWriter.AppendText(@"
h1 {
    font-family: Verdana;
    text-align: center;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

div.tiny {
    font-size: 7px;
    color: Gainsboro;
}", HtmlTextWriterTag.Style);
            htmlWriter.RenderEndTag();
        }

        private void createEncodedMessage(HtmlTextWriter htmlWriter)
        {
            htmlWriter.RenderBeginTag(HtmlTextWriterTag.Table);
            htmlWriter.RenderBeginTag(HtmlTextWriterTag.Tr);

            foreach (var encoding in _codedMessage.Generate())
            {
                if (encoding == Environment.NewLine)
                {
                    htmlWriter.RenderEndTag();
                    htmlWriter.RenderBeginTag(HtmlTextWriterTag.Tr);
                }
                else
                {
                    htmlWriter.AppendText(encoding, HtmlTextWriterTag.Td);
                }
            }

            htmlWriter.RenderEndTag();
            htmlWriter.RenderEndTag();
        }

        private static void writeHtmlToWebBrowser(WebBrowser webBrowser, StringWriter stringWriter)
        {
            webBrowser.Parent.Enabled = false; //https://stackoverflow.com/questions/8495857/webbrowser-steals-focus
            webBrowser.DocumentText = string.Empty;
            webBrowser.Document.OpenNew(true);
            webBrowser.Document.Write(stringWriter.ToString());
            webBrowser.Refresh();
            webBrowser.Parent.Enabled = true;
        }

        private void createHeading(HtmlTextWriter htmlWriter)
        {
            htmlWriter.AppendText(string.Format("{0}{1}{1}Maths Cypher{1}{1}{0}", "&#9760;", "&nbsp;"), HtmlTextWriterTag.H1);
            htmlWriter.AppendText("Can you solve this puzzle?",
                HtmlTextWriterTag.P);
        }

    }
}