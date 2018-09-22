full_name = lambda fn, ln: "{} {}".format(fn.strip().title(),
                                          ln.strip().title())
print(full_name("  liEvi", "silva"))

scifi_authors = [
    "Isaac Asimov", "Ray Bradbury", "Robert Heinslein", "Arthur C. Clarke",
    "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells",
    "Leigh Brackett"
]
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)


def build_quadratic_function(a, b, c):
    """Return the function f(x) = ax^2 + bx + c."""
    return lambda x: a * x**2 + b * x + c


f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(2))
print(build_quadratic_function(3, 0, 1)(2))