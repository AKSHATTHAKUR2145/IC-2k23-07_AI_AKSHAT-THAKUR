
import java.util.*;

public class DFSIterative {

    static void dfs(Map<Integer, List<Integer>> graph,
            int start) {

        Stack<Integer> stack = new Stack<>();
        Set<Integer> visited = new HashSet<>();

        stack.push(start);

        while (!stack.isEmpty()) {

            int current = stack.pop();

            if (visited.contains(current)) {
                continue;
            }

            visited.add(current);

            System.out.print(current + " ");

            // Add neighbors to stack
            for (int i = graph.get(current).size() - 1;
                    i >= 0;
                    i--) {

                int neighbor = graph.get(current).get(i);

                if (!visited.contains(neighbor)) {
                    stack.push(neighbor);
                }
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

        System.out.println("DFS Traversal:");

        dfs(graph, 0);
    }
}
