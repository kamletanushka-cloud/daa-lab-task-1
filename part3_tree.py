tree = {
    "Math": ["Algebra", "Geometry"],
    "Science": ["Physics", "Chemistry"]
}

print("Tree")

for subject in tree:
    print(subject)
    for child in tree[subject]:
        print("   |- ", child)

print()

print("Level Order Traversal")
print("Math")
print("Science")
print("Algebra")
print("Geometry")
print("Physics")
print("Chemistry")