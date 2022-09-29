import hypothesis
from hypothesis import strategies as st

class BasicAssertions:
    def create(self, data: st.DataObject):
        return

    @hypothesis.given(data=st.data())
    @hypothesis.settings(max_examples=20)
    def test_1(self, data: st.DataObject):
        self.create(data)
        data.draw(st.lists(st.integers(1, 5), min_size=2, max_size=5))


class Test_A(BasicAssertions):
    def create(self, data: st.DataObject):
        d1 = data.draw(st.sampled_from("abcd"))
        if d1 in "bc":
            d2 = True
        else:
            d2 = data.draw(st.booleans())
        d3 = True if d2 else data.draw(st.booleans())

        if not (d2 and d3):
            d4, d5 = 1, 1
        else:
            d4 = data.draw(st.sampled_from([1, 2, 3]))
            d5 = data.draw(st.integers(min_value=0, max_value=3))

        d6 = data.draw(st.lists(st.integers(1, 8), min_size=1, max_size=3))
        d7 = data.draw(st.sampled_from("ab"))


class Test_B(BasicAssertions):
    def create(self, data: st.DataObject):
        d1 = data.draw(st.sampled_from([1, 2, 3]))
        d2 = data.draw(st.sampled_from("abcd"))

        if d2 in "bc":
            d3 = True
        else:
            d3 = data.draw(st.booleans())

        d4 = data.draw(st.lists(st.integers(1, 8), min_size=1, max_size=3))
        d5 = data.draw(st.sampled_from("ab"))


class Test_C(BasicAssertions):
    def create(self, data: st.DataObject):
        d1 = data.draw(st.sampled_from("ab"))
        d2 = data.draw(st.sampled_from("abcd"))

        if d2 in "bc":
            d3 = True
        else:
            d3 = data.draw(st.booleans())

        d4 = True if d3 else data.draw(st.booleans())

        if not d3 and not d4 and d1 == "a":
            d5, d6 = 1, 1
        else:
            d5 = data.draw(st.sampled_from([1, 2, 3]))
            d6 = data.draw(st.integers(min_value=0, max_value=3))

        d7 = data.draw(st.lists(st.integers(1, 8), min_size=1, max_size=3))
        d8 = data.draw(st.sampled_from("ab"))
