import java.util.*;

public class ProductionSystem {

    static Map<String, String> facts = new HashMap<>();

    static class Rule {
        String condition;
        String conclusion;

        Rule(String condition, String conclusion) {
            this.condition = condition;
            this.conclusion = conclusion;
        }
    }

    public static void main(String[] args) {

        // Initial facts
        facts.put("temperature", "high");
        facts.put("sky", "cloudy");

        // Production rules
        List<Rule> rules = new ArrayList<>();

        rules.add(new Rule(
                "temperature=high",
                "weather=hot"
        ));

        rules.add(new Rule(
                "sky=cloudy",
                "rain=possible"
        ));

        rules.add(new Rule(
                "weather=hot",
                "drink=water"
        ));

        // Inference Engine
        boolean changed = true;

        while (changed) {
            changed = false;

            for (Rule rule : rules) {

                String[] condition =
                        rule.condition.split("=");

                String key = condition[0];
                String value = condition[1];

                if (facts.containsKey(key)
                        && facts.get(key).equals(value)) {

                    String[] conclusion =
                            rule.conclusion.split("=");

                    String cKey = conclusion[0];
                    String cValue = conclusion[1];

                    if (!facts.containsKey(cKey)) {

                        facts.put(cKey, cValue);

                        System.out.println(
                                "Rule Fired: "
                                + rule.condition
                                + " -> "
                                + rule.conclusion
                        );

                        changed = true;
                    }
                }
            }
        }

        System.out.println("\nFinal Knowledge:");

        for (Map.Entry<String, String> entry : facts.entrySet()) {
            System.out.println(
                    entry.getKey() + " = " + entry.getValue()
            );
        }
    }
}