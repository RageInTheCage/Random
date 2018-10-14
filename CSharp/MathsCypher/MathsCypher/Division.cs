using System;
using System.Collections.Generic;
using System.Linq;

namespace MathsCypher
{
    internal class Division
    {
        public Division(int answer, Random random, int maxDividendValue = 144)
        {
            var factorPairs = getFactorPairs(answer, maxDividendValue)
                .ToList();

            var factorPair = getRandomFactorPair(random, factorPairs);

            _divisor = factorPair.Factor1;
            _dividend = answer * _divisor;
        }

        private int _divisor;
        private int _dividend;

        private static FactorPair getRandomFactorPair(Random random, List<FactorPair> factors)
        {
            int index = random.Next(0, factors.Count);
            return factors[index];
        }

        private IEnumerable<FactorPair> getFactorPairs(int answer, int maxDividendValue)
        {
            for (int factor1 = 2; factor1 <= 12; factor1++)
            {
                if (factor1 * answer > maxDividendValue)
                    yield break;
                
                yield return new FactorPair(factor1, answer);
            }
        }

        public override string ToString()
        {
            return string.Format("{0} ÷ {1}   ", _dividend, _divisor);
        }
    }
}