import bs4
import re
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
            title_full = title_root.find("tbody").find("tr").find("td", class_=" MaskRenderer").text

            lecture_nr = title_full.split(" ", 1)[0]
            title = title_full.split(" ", 1)[1].split(" (", 1)[0]

            resource['lecture_title_full'] = title_full
            resource['lecture_title'] = title
            resource['lecture_nr'] = lecture_nr

            semester_match = re.search('((?:WS|SS) \d\d\d\d/\d\d)', 'IN2028 Business Analytics (4SWS FA, WS 2016/17)')
            if semester_match:
                semester = semester_match.group()
            else:
                raise ValueError('No semester found!')
            resource['semester'] = semester

        else:
            raise ValueError("No course title found!")

        resource['course_stats'] = self._extract_course_stats(soup)

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
