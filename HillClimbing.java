
public class HillClimbing {

    static int[] values = {1, 3, 5, 8, 6, 4, 2};

    static int hillClimbing(int start) {

        int current = start;

        while (true) {

            int left = current - 1;
            int right = current + 1;

            int best = current;

            // Check left neighbor
            if (left >= 0
                    && values[left] > values[best]) {

                best = left;
            }

            // Check right neighbor
            if (right < values.length
                    && values[right] > values[best]) {

                best = right;
            }

            // No better neighbor
            if (best == current) {
                break;
            }

            current = best;
        }

        return current;
    }

    public static void main(String[] args) {

        int start = 0;

        int result = hillClimbing(start);

        System.out.println("Hill Climbing Search");

        System.out.println("Starting Position: " + start);

        System.out.println("Best Position: " + result);

        System.out.println("Maximum Value: "
                + values[result]);
    }
}
