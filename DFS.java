
import java.util.*;

public class DFS {

    static void dfs(Map<Integer, List<Integer>> graph,
            int current,
            Set<Integer> visited) {

        visited.add(current);

        System.out.print(current + " ");

        for (int neighbor : graph.get(current)) {

            if (!visited.contains(neighbor)) {

                dfs(graph, neighbor, visited);
            }
        }
    }

    public static void main(String[] args) {

        Map<Integer, List<Integer>> graph = new HashMap<>();

        graph.put(0, Arrays.asList(1, 2));
        graph.put(1, Arrays.asList(3, 4));
        graph.put(2, Arrays.asList(5, 6));
        graph.put(3, new ArrayList<>());
        graph.put(4, new ArrayList<>());
        graph.put(5, new ArrayList<>());
        graph.put(6, new ArrayList<>());

        Set<Integer> visited = new HashSet<>();

        System.out.println("DFS Traversal:");

        dfs(graph, 0, visited);
    }
}
