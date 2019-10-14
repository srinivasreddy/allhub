from tests.utils import allhub


class TestIterator:
    def test_with_iterator_defaults(self):
        for index, response in enumerate(
            allhub.iterator(allhub.all_organizations), start=1
        ):
            assert len(response) == 30
            assert allhub.page == index
            assert allhub.per_page == 30
            if index == 4:
                break
        else:
            assert False, "There are not even 3*30 = 90 orgs in Github ;)"

    def test_without_iterator(self):
        response = allhub.all_organizations()
        assert len(response) == 30
        assert response is not None
        assert allhub.page == 1
        assert allhub.per_page == 30

    def test_with_nth_page_default_per_page(self):
        response = allhub.all_organizations(page=10)
        assert allhub.page == 10
        assert allhub.per_page == 30
        assert len(response) == 30
        assert response is not None

    def test_with_custom_per_page_and_default_page(self):
        response = allhub.all_organizations(per_page=100)
        assert allhub.page == 1
        assert allhub.per_page == 100
        assert len(response) == 100
        assert response is not None

    def test_with_nth_page_and_per_page_results(self):
        response = allhub.all_organizations(page=10, per_page=40)
        assert allhub.page == 10
        assert allhub.per_page == 40
        assert len(response) == 40
        assert response is not None

    def test_with_num_pages_and_one_time_function_call(self):
        """
        Without iterator num_pages is ignored.
        """
        response = allhub.all_organizations(num_pages=10)
        assert allhub.page == 1
        assert allhub.per_page == 30
        assert len(response) == 30
        assert response is not None

    def test_iterator_with_all_custom_params(self):
        for counter, response in enumerate(
            allhub.iterator(
                allhub.all_organizations, page=1, per_page=50, num_pages=10
            ),
            start=1,
        ):
            assert allhub.per_page == 50
            assert allhub.page == counter
            assert len(response) == 50
            assert response is not None
        assert counter == 10
