# Copyright 2018, Erlang Solutions Ltd, and S2HC Sweden AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

ATOM_MARKER = "pyrlang.Atom"


class Atom(str):
    """ Stores a string decoded from Erlang atom. Encodes back to atom.

        Be ware this won't separate itself from a string in a dict for example:

            {Atom('foo'): 1, 'foo': 2} == {'foo': 2}
    """
    def __repr__(self):
        return'Atom({})'.format(super(Atom, self).__repr__())


class StrictAtom(Atom):
    """
    Stores a string decoded from Erlang atom. Encodes back to atom.

    Can serve as a Python dictionary key besides str with same content:w

        {StrictAtom('foo'): 1, 'foo': 2} == {StrictAtom('foo'): 1, 'foo': 2}

    """
    def __repr__(self) -> str:
        return "Strict{}".format(super(StrictAtom, self).__repr__())

    def __str__(self):
        return self.__repr__()

    def __hash__(self):
        return hash((ATOM_MARKER, super(StrictAtom, self).__hash__()))
