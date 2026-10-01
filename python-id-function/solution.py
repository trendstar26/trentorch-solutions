def did_mutate_in_place(lst: list, operation) -> bool:
    x=id(lst)
    z=operation(lst)
    
    if z is not None:
      lst=z
      
    y=id(lst)
    return x==y
    """
    `operation` is a function that takes a list and either
    mutates it in place and returns None (e.g. lambda l:
    l.append(99)), or returns a brand-new list without touching
    the original (e.g. lambda l: l + [99]).

    Record id(lst) before calling operation(lst). Call
    operation(lst). If it returned something other than None,
    that return value is the list to use going forward (reassign
    your local `lst` reference to it). Record id() again on
    whichever list you're now referencing.

    Return True if the id() is unchanged (mutated in place),
    False if it changed (a new list was created).
    """
    pass


def are_same_object(a, b) -> bool:
    if id(a)==id(b):
      return True 
    else:
      return False
    """
    Return True if `a` and `b` refer to the exact same object,
    using id() — not ==.
    """
    pass
