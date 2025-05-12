"""stt module, created, built and maintained by JoBe"""
# MIT License

# Copyright (c) 2025, JoBe

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Note that this module is not typed, 
# as it might be used with Python < 3.6

__all__ = [
    "",
]


def dump(tree, *, file=sys.stdout):
    # There is no call to the
    # `_check_validity` function,
    # as we can also dump invalid
    # trees, as long as they are
    # traverseable.
    if not _is_traversable(tree):
        raise TypeError(f"expected stt tree instance, got {tree}")
    # If the tree is already in 
    # the right form, this call
    # won't change it.
    iterable_tree = _reconstruct(tree)
    for node in iter(iterable_tree):
        print(_reconstruct_node(node), file=file)
        
