import java.util.*;

public class BestFirstSearch {

    static class Node {
        int value;
        int heuristic;

        Node(int value, int heuristic) {
            this.value = value;
            this.heuristic = heuristic;
        }
    }

    static void bestFirstSearch(
            Map<Integer, List<Integer>> graph,
            Map<Integer, Integer> heuristic,
            int start,
            int goal) {

        PriorityQueue<Node> queue =
                new PriorityQueue<>(
                        Comparator.comparingInt(
                                node -> node.heuristic
                        )
                );

        Set<Integer> visited = new HashSet<>();

        queue.add(
                new Node(start, heuristic.get(start))
        );

        while (!queue.isEmpty()) {

            Node current = queue.poll();

            if (visited.contains(current.value)) {
                continue;
            }

            visited.add(current.value);

            System.out.print(current.value + " ");

            if (current.value == goal) {
                System.out.println("\nGoal Found!");
                return;
            }

            for (int neighbor : graph.get(current.value)) {

                if (!visited.contains(neighbor)) {

                    queue.add(
                            new Node(
                                    neighbor,
                                    heuristic.get(neighbor)
                            )
                    );
                }
            }
        }

        System.out.println("\nGoal Not Found!");
    }

    public static void main(String[] args) {

        Map<Integer, List<Integer>> graph =
                new HashMap<>();

        graph.put(0, Arrays.asList(1, 2));
        graph.put(1, Arrays.asList(3, 4));
        graph.put(2, Arrays.asList(5, 6));
        graph.put(3, new ArrayList<>());
        graph.put(4, new ArrayList<>());
        graph.put(5, new ArrayList<>());
        graph.put(6, new ArrayList<>());

        // Lower value = closer to goal
        Map<Integer, Integer> heuristic =
                new HashMap<>();

        heuristic.put(0, 6);
        heuristic.put(1, 4);
        heuristic.put(2, 2);
        heuristic.put(3, 5);
        heuristic.put(4, 3);
        heuristic.put(5, 1);
        heuristic.put(6, 0);

        System.out.println("Best First Search:");

        bestFirstSearch(
                graph,
                heuristic,
                0,
                6
        );
    }
}