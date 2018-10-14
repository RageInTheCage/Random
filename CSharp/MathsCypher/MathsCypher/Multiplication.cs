using System;
using System.Collections.Generic;
using System.Linq;

namespace MathsCypher
{
    internal class Multiplication
    {
        public readonly int Answer;
        public readonly int Factor1;
        public readonly int Factor2;

        private Random _random;

        public Multiplication(int answer, Random random)
        {
            Answer = answer;
            _random = random;

            Factor1 = getRandomFactor();
            Factor2 = answer / Factor1;

        }

        private int getRandomFactor()
        {
            var factors = Answer.GetFactors()
                .OrderBy(f => f)
                .ToList();

            var minFactor = 1;
            var maxFactor = factors.Count;

            if (factors.Count > 2)
            {
                minFactor++;
                maxFactor--;
            }

            int index = _random.Next(minFactor, maxFactor);

            return factors[index - 1];
        }

        public override string ToString()
        {
            return string.Format("{0} x {1}   ", Factor1, Factor2);
        }
    }
}