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

        public HTMLCodedMessage(CodedMessage codedMessage, Dictionary<char, int> mappings)
        {
            _codedMessage = codedMessage;
            _mappings = mappings;
        }

        public string Generate()
        {
            using (var stringWriter = new StringWriter())
            using (var htmlWriter = new HtmlTextWriter(stringWriter))
            {
                htmlWriter.RenderBeginTag(HtmlTextWriterTag.Html);
                createHead(htmlWriter);
                createBody(htmlWriter);
                htmlWriter.RenderEndTag();

                return stringWriter.ToString();
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

td {
    padding: 8px;
}

td.question {
    text-align: center;
}

td.answer {
    border: 3px dotted red;
    height: 35px;
    line-height: 2;
}

td.gap {
    width: 1px;
}

div.tiny {
    font-size: 7px;
    color: Gainsboro;
}", HtmlTextWriterTag.Style);
            htmlWriter.RenderEndTag();
        }

        private void createEncodedMessage(HtmlTextWriter htmlWriter)
        {
            startRenderingTable(htmlWriter);

            var letterCount = 0;
            foreach (var encodedCharacter in _codedMessage.Generate())
            {
                if (encodedCharacter == Environment.NewLine)
                {
                    renderAnswerRow(htmlWriter, letterCount);
                    letterCount = 0;
                    continue;
                }

                renderQuestion(htmlWriter, encodedCharacter);
                letterCount++;
            }
            renderAnswerRow(htmlWriter, letterCount);

            endRenderingTable(htmlWriter);
        }

        private static void renderQuestion(HtmlTextWriter htmlWriter, string encodedCharacter)
        {
            htmlWriter.AddAttribute(HtmlTextWriterAttribute.Class, "question");
            htmlWriter.AppendText(encodedCharacter, HtmlTextWriterTag.Td);
            renderCellGap(htmlWriter);
        }

        private void renderAnswerRow(HtmlTextWriter htmlWriter, int letterCount)
        {
            startRenderingNextRow(htmlWriter);
            for (int letter = 0; letter < letterCount; letter++)
            {
                htmlWriter.AddAttribute(HtmlTextWriterAttribute.Class, "answer");
                htmlWriter.RenderBeginTag(HtmlTextWriterTag.Td);
                htmlWriter.RenderEndTag();

                renderCellGap(htmlWriter);
            }
            startRenderingNextRow(htmlWriter);
        }

        private static void renderCellGap(HtmlTextWriter htmlWriter)
        {
            htmlWriter.AddAttribute(HtmlTextWriterAttribute.Class, "gap");
            htmlWriter.RenderBeginTag(HtmlTextWriterTag.Td);
            htmlWriter.RenderEndTag();
        }

        private static void endRenderingTable(HtmlTextWriter htmlWriter)
        {
            htmlWriter.RenderEndTag();
            htmlWriter.RenderEndTag();
        }

        private static void startRenderingNextRow(HtmlTextWriter htmlWriter)
        {
            htmlWriter.RenderEndTag();
            htmlWriter.RenderBeginTag(HtmlTextWriterTag.Tr);
        }

        private static void startRenderingTable(HtmlTextWriter htmlWriter)
        {
            htmlWriter.RenderBeginTag(HtmlTextWriterTag.Table);
            htmlWriter.RenderBeginTag(HtmlTextWriterTag.Tr);
        }

        private void createHeading(HtmlTextWriter htmlWriter)
        {
            htmlWriter.AppendText(string.Format("{0}{1}{1}Maths Cypher{1}{1}{0}", "&#9760;", "&nbsp;"), HtmlTextWriterTag.H1);
            htmlWriter.AppendText("Can you solve this puzzle?",
                HtmlTextWriterTag.P);
        }

    }
}