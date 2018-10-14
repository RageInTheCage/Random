using System;
using System.Collections.Generic;
using System.Linq;

namespace MathsCypher
{
    public class Multiplication
    {
        public readonly FactorPair Factors = FactorPair.Empty;

        public Multiplication(int answer, Random random, int maxFactorValue = 12)
        {
            var factorPairs = getFactorPairs(answer, maxFactorValue)
                .ToList();
            
            if (factorPairs.Count > 0)
                Factors = getRandomFactorPair(random, factorPairs);
        }

        private static FactorPair getRandomFactorPair(Random random, List<FactorPair> factors)
        {
            int index = random.Next(0, factors.Count);
            return factors[index];
        }

        private static IEnumerable<FactorPair> getFactorPairs(int answer, int maxFactorValue)
        {
            return answer.GetFactors()
                .Where(f => f > 1 && f < answer & f <= maxFactorValue)
                .Select(f => new FactorPair(f, answer / f))
                .Where(fp => fp.Factor2 <= maxFactorValue);
        }

        public override string ToString()
        {
            return string.Format("{0} x {1}   ", Factors.Factor1, Factors.Factor2);
        }
    }
}