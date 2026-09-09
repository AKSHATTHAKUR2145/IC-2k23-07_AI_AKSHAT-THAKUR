import java.util.*;

public class WaterJugProblem {

    static class State {
        int jug1;
        int jug2;

        State(int jug1, int jug2) {
            this.jug1 = jug1;
            this.jug2 = jug2;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj)
                return true;

            if (!(obj instanceof State))
                return false;

            State other = (State) obj;
            return jug1 == other.jug1 && jug2 == other.jug2;
        }

        @Override
        public int hashCode() {
            return Objects.hash(jug1, jug2);
        }
    }

    static void solve(int capacity1, int capacity2, int target) {

        Queue<State> queue = new LinkedList<>();
        Set<State> visited = new HashSet<>();
        Map<State, State> parent = new HashMap<>();
        Map<State, String> action = new HashMap<>();

        State start = new State(0, 0);

        queue.add(start);
        visited.add(start);
        parent.put(start, null);
        action.put(start, "Start");

        State finalState = null;

        while (!queue.isEmpty()) {

            State current = queue.poll();

            // Check if target is achieved
            if (current.jug1 == target || current.jug2 == target) {
                finalState = current;
                break;
            }

            // Generate all possible next states

            // 1. Fill Jug 1
            State next = new State(capacity1, current.jug2);

            if (!visited.contains(next)) {
                visited.add(next);
                queue.add(next);
                parent.put(next, current);
                action.put(next, "Fill Jug 1");
            }

            // 2. Fill Jug 2
            next = new State(current.jug1, capacity2);

            if (!visited.contains(next)) {
                visited.add(next);
                queue.add(next);
                parent.put(next, current);
                action.put(next, "Fill Jug 2");
            }

            // 3. Empty Jug 1
            next = new State(0, current.jug2);

            if (!visited.contains(next)) {
                visited.add(next);
                queue.add(next);
                parent.put(next, current);
                action.put(next, "Empty Jug 1");
            }

            // 4. Empty Jug 2
            next = new State(current.jug1, 0);

            if (!visited.contains(next)) {
                visited.add(next);
                queue.add(next);
                parent.put(next, current);
                action.put(next, "Empty Jug 2");
            }

            // 5. Pour Jug 1 -> Jug 2
            int transfer = Math.min(
                    current.jug1,
                    capacity2 - current.jug2
            );

            next = new State(
                    current.jug1 - transfer,
                    current.jug2 + transfer
            );

            if (!visited.contains(next)) {
                visited.add(next);
                queue.add(next);
                parent.put(next, current);
                action.put(next, "Pour Jug 1 -> Jug 2");
            }

            // 6. Pour Jug 2 -> Jug 1
            transfer = Math.min(
                    current.jug2,
                    capacity1 - current.jug1
            );

            next = new State(
                    current.jug1 + transfer,
                    current.jug2 - transfer
            );

            if (!visited.contains(next)) {
                visited.add(next);
                queue.add(next);
                parent.put(next, current);
                action.put(next, "Pour Jug 2 -> Jug 1");
            }
        }

        // No solution
        if (finalState == null) {
            System.out.println("No solution exists.");
            return;
        }

        // Reconstruct path
        List<State> path = new ArrayList<>();

        State current = finalState;

        while (current != null) {
            path.add(current);
            current = parent.get(current);
        }

        Collections.reverse(path);

        // Print solution
        System.out.println("Solution:");

        for (int i = 0; i < path.size(); i++) {

            State state = path.get(i);

            if (i == 0) {
                System.out.println(
                        "Start -> (" + state.jug1 + ", " + state.jug2 + ")"
                );
            } else {
                System.out.println(
                        action.get(state)
                        + " -> ("
                        + state.jug1
                        + ", "
                        + state.jug2
                        + ")"
                );
            }
        }

        System.out.println("\nTotal steps: " + (path.size() - 1));
    }

    public static void main(String[] args) {

        int jug1Capacity = 4;
        int jug2Capacity = 3;
        int target = 2;

        solve(jug1Capacity, jug2Capacity, target);
    }
}