
import java.util.*;

public class BFSshortestPath {

    static void bfs(Map<Integer, List<Integer>> graph,
            int start, int goal) {

        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        Map<Integer, Integer> parent = new HashMap<>();

        queue.add(start);
        visited.add(start);
        parent.put(start, -1);

        while (!queue.isEmpty()) {

            int current = queue.poll();

            if (current == goal) {
                break;
            }

            for (int neighbor : graph.get(current)) {

                if (!visited.contains(neighbor)) {

                    visited.add(neighbor);
                    queue.add(neighbor);
                    parent.put(neighbor, current);
                }
            }
        }

        if (!visited.contains(goal)) {
            System.out.println("Path not found");
            return;
        }

        // Create path
        List<Integer> path = new ArrayList<>();

        int current = goal;

        while (current != -1) {
            path.add(current);
            current = parent.get(current);
        }

        Collections.reverse(path);

        System.out.println("Shortest Path:");

        for (int node : path) {
            System.out.print(node + " ");
        }

        System.out.println();
        System.out.println("Number of edges: " + (path.size() - 1));
    }

    public static void main(String[] args) {

        Map<Integer, List<Integer>> graph = new HashMap<>();

        graph.put(0, Arrays.asList(1, 2));
        graph.put(1, Arrays.asList(0, 3, 4));
        graph.put(2, Arrays.asList(0, 5));
        graph.put(3, Arrays.asList(1));
        graph.put(4, Arrays.asList(1, 5));
        graph.put(5, Arrays.asList(2, 4));

        bfs(graph, 0, 5);
    }
}
