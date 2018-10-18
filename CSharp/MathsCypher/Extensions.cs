using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Web.UI;
using System.Windows.Forms;

namespace MathsCypher
{
    public static class Extensions
    {
        public static void AppendText(this HtmlTextWriter htmlWriter,
            string contents, HtmlTextWriterTag tag)
        {
            htmlWriter.RenderBeginTag(tag);
            htmlWriter.Write(contents);
            htmlWriter.RenderEndTag();
        }


        public static List<TValue> Shuffle<TValue>(this List<TValue> source)
        {
            Random random = new Random();
            return source.OrderBy(x => random.Next())
               .ToList();
        }

        public static List<int> GetFactors(this int number)
        {
            List<int> factors = new List<int>();
            int max = (int)Math.Sqrt(number);  //round down
            for (int factor = 1; factor <= max; ++factor)
            { //test from 1 to the square root, or the int below it, inclusive.
                if (number % factor == 0)
                {
                    factors.Add(factor);
                    if (factor != number / factor)
                    { // Don't add the square root twice!  Thanks Jon
                        factors.Add(number / factor);
                    }
                }
            }
            return factors;
        }

        public static int ConvertToIntegerOrDefault(this string stringValue, int defaultValue)
        {
            int value;

            return int.TryParse(stringValue, out value) ? value : defaultValue;
        }
    }
}