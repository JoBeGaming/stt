# stt module in Python.

# (c) JoBe, 2025


import sys


__all__ = [
    "dump",
    "dump_iterable"
]


class STTError(Exception):
    """
    Base class for all STT
    related errors.
    """


def _walk_tree(tree, /, *, level = 0):
    """
    Return a tuple of all nodes with their 'indentation' level and the corresponding node.  
    The boolean is used to indicate any number of said argument following, if True:

        >>> t = a[b, c, d[e, ...]], f
        ...
        >>> print(_walk_tree(t))
        ((0, a, False), (1, b, False), (1, c, False), 
        (1, d, False), (2, e, True), (0, f, False))

    In edge-cases, like `t = ...`, `None` is returned.  
    Note that the tree is not checked for validity
    """

    final = []
    if not isinstance(tree, tuple):
        tree = (tree,)
    if tree == (...,):
        return None

    for tp in tree:
        if tp is ...:

            for index_of_ellipsis_owner in range(len(final) - 1, -1, -1):
                if final[index_of_ellipsis_owner][0] == level:
                    prev_args = final[index_of_ellipsis_owner][:-1]
                    final[index_of_ellipsis_owner] = (prev_args + (True,))
                    break
            continue
        
        origin = _get_node_origin(tp, allow_none=True, allow_all=True)
        args = _get_node_args(tp, allow_all=True)
        if origin is None:
            final.append((level, tp, False))
        
        else:
            final.append((level, origin, False))
            inner = _walk_tree(args, level=level + 1)
            if inner:
                final.extend(inner)
    return tuple(final)


def _is_traversable(tree):
    """
    Check if the tree is traversable.
    Internally this is done by calling
    both `_walk_tree` and `_reconstruct` 
    and catching Errors.
    """

    try:
        _walk_tree(tree)
        return True
    except (TypeError, KeyError, IndexError):
        return False


def _str_of_node(node):
    ...


def _is_reconstructed(tree):
    return False


def _reconstruct(tree):
    if _is_reconstructed(tree):
        return tree
    
    final = ()
    counter = 0
    prev_level = 0
    
    for level, node, ellipsis_following in tree:
        
        if counter == 0:
            final += (node,)
            if ellipsis_following:
                final += (...,)
        
        if level > prev_level:
                ...
        elif level < prev_level:
                ...
        else: 
                ...
        counter += 1


def _reconstruct_node(node):
    if node[2]:
        return f"|{'-' * node[0]} {node[1]}/n|{'-' * node[0]} ..."
    return f"|{'-' * node[0]} {node[1]}"


def _check_validity(tree, msg = ""):
    ...


def _make_iterable(tree):
    return _walk_tree(tree)


def dump(tree, *, file=sys.stdout):
    """
    Dump the given tree, e.g.:

    >>> Tree = a[b, c, d[e, ...], f]
    >>> dump(Tree)
    |- a
    |-- b
    |-- c
    |-- d
    |--- e
    |--- ...
    |-- f

    Note that the order is preserved.
    The tree is not checked for validity.
    """

    # There is no call to the
    # `_check_validity` function,
    # as we can also dump invalid
    # trees, as long as they are
    # traversable.

    if not _is_traversable(tree):
        raise TypeError("expected stt tree instance, got" +  str(tree))

    # If the tree is already in 
    # the right form, this call
    # won't change it, except 
    # for making it iterable

    iterable_tree = _make_iterable(_reconstruct(tree))
    for node in iterable_tree:
        print(_reconstruct_node(node), file=file)


def dump_iterable(tree):
    """
    Dump the given tree as a generator, e.g.:

    >>> Tree = a[b, c, d[e, ...], f]
    >>> for node in dump_iterable(Tree):
    ...     print(node)
    ...
    |- a
    |-- b
    |-- c
    |-- d
    |--- e
    |--- ...
    |-- f

    Note that the order is preserved.
    The tree is not checked for validity.
    """

    # There is no call to the
    # `_check_validity` function,
    # as we can also dump invalid
    # trees, as long as they are
    # traversable.

    if not _is_traversable(tree):
        raise TypeError("expected stt tree instance, got" +  str(tree))

    # If the tree is already in 
    # the right form, this call
    # won't change it, except 
    # for making it iterable

    iterable_tree = _make_iterable(_reconstruct(tree))
    for node in iterable_tree:
        yield _reconstruct_node(node)
