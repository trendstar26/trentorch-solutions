def mutate_list(lst: list) -> None:
    lst.append(4)
    return None
    """
    Mutate `lst` in place by appending the value 4 to it.
    Do not reassign lst to a new object. Return nothing.
    """
    pass


def reassign_list(lst: list) -> list:
    
    return [9,9,9]
    """
    Create a brand-new list [9, 9, 9] and return it, without
    mutating the original `lst` in any way.
    """
    pass


def observe_through_alias(original: list) -> dict:
    alias=original
    original.append(100)
    alias_after=list(alias)
    original=[0,0,0]
    alias_after2=list(alias)
    return {
        "alias_after_mutation": alias_after,
        "alias_after_reassignment":  alias_after2,
        "original_final": original
      }

    
  
    """
    Inside this function:
      1. Create `alias = original` (a second variable pointing
         at the same object).
      2. Mutate `original` by appending 100 to it.
      3. Reassign `original` to a brand-new list [0, 0, 0]
         (do not mutate this new list into alias's object).

    Return a dictionary:
      {
        "alias_after_mutation": <contents of alias right after step 2>,
        "alias_after_reassignment": <contents of alias right after step 3>,
        "original_final": <contents of original at the end>
      }
    """
    pass
