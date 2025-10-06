
"""
Module d'encodage de chaînes de caractères en liste de tuples
(caractère, nombre d'occurrences consécutives).
"""
from typing import List, Tuple

def artcode_i(s: str) -> List[Tuple[str, int]]:
    """
    Encode une chaîne en liste de tuples (caractère, nombre d'occurrences consécutives).
    Version itérative.
    Args:
        s (str): chaîne à encoder
    Returns:
        List[Tuple[str, int]]: liste de tuples (caractère, nombre d'occurrences)
    """
    if not s:
        return []
    chars = [s[0]]
    occs = [1]
    k = 1
    n = len(s)
    while k < n:
        if s[k] == s[k - 1]:
            occs[-1] += 1
        else:
            chars.append(s[k])
            occs.append(1)
        k += 1
    return list(zip(chars, occs))

def artcode_r(s: str) -> List[Tuple[str, int]]:
    """
    Encode une chaîne en liste de tuples (caractère, nombre d'occurrences consécutives).
    Version récursive.
    Args:
        s (str): chaîne à encoder
    Returns:
        List[Tuple[str, int]]: liste de tuples (caractère, nombre d'occurrences)
    """
    if not s:
        return []
    first = s[0]
    i = 1
    n = len(s)
    while i < n and s[i] == first:
        i += 1
    return [(first, i)] + artcode_r(s[i:])

def main() -> None:
    """
    Fonction principale pour tester l'encodage itératif et récursif.
    """
    chaine = "MMMMaaacXolloMM"
    print("Chaîne :", chaine)
    print("Itératif :", artcode_i(chaine))
    print("Récursif :", artcode_r(chaine))

if __name__ == "__main__":
    main()
