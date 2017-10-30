import bs4
from pathlib import Path

import parselib.common as common


class TUMCourseResourceFinder:
    pass


class TUMCourseStatisticExtractor:
    def __init__(self):
        self.source = "TUM"
        self.stats = CourseStatistics()

    @staticmethod
    def _extract_course_stats(soup):  # TODO
        course_data = {}

        return course_data

    def get_resource(self, filename):
        resource = {}

        file = Path(__file__).parents[1] / 'data' / filename

        page = open(file)
        soup = bs4.BeautifulSoup(page.read(), "lxml")

        title_root = soup.find("div", class_="MaskData")
        if title_root is not None:
            title = title_root.find("tbody").find("tr").find("td", class_=" MaskRenderer").text
            resource['title'] = title
        else:
            raise ValueError("No course title found!")

        resource['course_data'] = self._extract_course_stats(soup)

        return resource


class CourseStatistics:
    pass


if __name__ == "__main__":
    # common.test_resource_finder(
    #     TUMCourseResourceFinder()
    # )

    common.test_resource_extractor(
        TUMCourseStatisticExtractor(),
        "Business_Analytics.html"
    )
