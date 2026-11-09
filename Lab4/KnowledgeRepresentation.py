"""Rule-based reasoning, predicates, semantic network and frames."""
facts={"has_fever":True,"has_cough":True,"has_rash":False}
rules=[
    (lambda f:f.get("has_fever") and f.get("has_cough"),"possible_respiratory_infection"),
    (lambda f:f.get("has_fever") and f.get("has_rash"),"possible_viral_rash"),
]
def infer(facts):
    conclusions=[]
    for condition,conclusion in rules:
        if condition(facts): conclusions.append(conclusion)
    return conclusions

# Semantic network represented as edges: (subject, relation, object)
semantic_network=[
    ("Student","is-a","Person"),("Person","has","Name"),
    ("Student","enrolled-in","University"),("University","offers","Course")
]

# Frame representation
frames={
    "Student":{"slots":{"name":"unknown","roll_no":"unknown","course":"MCA"}},
    "Course":{"slots":{"name":"AI","duration":"5 years","level":"Integrated"}}
}

if __name__=="__main__":
    print("Rule inference:",infer(facts))
    print("Semantic network:",semantic_network)
    print("Student frame:",frames["Student"])
