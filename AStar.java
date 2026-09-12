
import java.util.*;

public class AStar {

    static class Node implements Comparable<Node> {

        int value;
        int g;
        int h;

        Node(int value, int g, int h) {
            this.value = value;
            this.g = g;
            this.h = h;
        }

        int f() {
            return g + h;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.f(), other.f());
        }
    }

    static void aStar(
            Map<Integer, List<Integer>> graph,
            Map<String, Integer> cost,
            Map<Integer, Integer> heuristic,
            int start,
            int goal) {

        PriorityQueue<Node> queue
                = new PriorityQueue<>();

        Map<Integer, Integer> distance
                = new HashMap<>();

        Map<Integer, Integer> parent
                = new HashMap<>();

        for (int node : graph.keySet()) {
            distance.put(node, Integer.MAX_VALUE);
        }

        distance.put(start, 0);

        queue.add(
                new Node(
                        start,
                        0,
                        heuristic.get(start)
                )
        );

        while (!queue.isEmpty()) {

            Node current = queue.poll();

            int currentNode = current.value;

            // Goal reached
            if (currentNode == goal) {

                printPath(parent, start, goal);

                System.out.println(
                        "Total Cost: "
                        + distance.get(goal)
                );

                return;
            }

            for (int neighbor
                    : graph.get(currentNode)) {

                String edge
                        = currentNode + "-" + neighbor;

                int edgeCost = cost.get(edge);

                int newG
                        = distance.get(currentNode)
                        + edgeCost;

                if (newG < distance.get(neighbor)) {

                    distance.put(
                            neighbor,
                            newG
                    );

                    parent.put(
                            neighbor,
                            currentNode
                    );

                    queue.add(
                            new Node(
                                    neighbor,
                                    newG,
                                    heuristic.get(neighbor)
                            )
                    );
                }
            }
        }

        System.out.println("Goal Not Found!");
    }

    static void printPath(
            Map<Integer, Integer> parent,
            int start,
            int goal) {

        List<Integer> path
                = new ArrayList<>();

        int current = goal;

        path.add(current);

        while (current != start) {

            current = parent.get(current);

            path.add(current);
        }

        Collections.reverse(path);

        System.out.println("A* Path:");

        for (int node : path) {

            System.out.print(node + " ");
        }

        System.out.println();
    }

    public static void main(String[] args) {

        Map<Integer, List<Integer>> graph
                = new HashMap<>();

        graph.put(0, Arrays.asList(1, 2));
        graph.put(1, Arrays.asList(3, 4));
        graph.put(2, Arrays.asList(5, 6));
        graph.put(3, new ArrayList<>());
        graph.put(4, new ArrayList<>());
        graph.put(5, Arrays.asList(6));
        graph.put(6, new ArrayList<>());

        // Edge costs
        Map<String, Integer> cost
                = new HashMap<>();

        cost.put("0-1", 2);
        cost.put("0-2", 4);

        cost.put("1-3", 5);
        cost.put("1-4", 2);

        cost.put("2-5", 3);
        cost.put("2-6", 8);

        cost.put("5-6", 1);

        // Heuristic values
        Map<Integer, Integer> heuristic
                = new HashMap<>();

        heuristic.put(0, 6);
        heuristic.put(1, 5);
        heuristic.put(2, 4);
        heuristic.put(3, 7);
        heuristic.put(4, 4);
        heuristic.put(5, 1);
        heuristic.put(6, 0);

        System.out.println("A* Search:");

        aStar(
                graph,
                cost,
                heuristic,
                0,
                6
        );
    }
}
