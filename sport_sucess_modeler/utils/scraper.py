""" NFL Stats Scraper
"""
import requests
from bs4 import BeautifulSoup


class NFLStats:
    def __init__(self, year: str):
        self.year = str(year)

    def _pull_stats(self, url):
        """Pull data from html table.
        """
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Get Headers
        header = []
        for col in soup.find('table').find_all('th'):
            header.append(col.get_text())

        teams = {}

        # Loop through table rows
        for row in soup.find('table').find('tbody').find_all('tr'):
            team = row.find('td').find('div', {
                'class': 'd3-o-club-fullname'}).get_text().replace('\n', '').replace(' ', '')
            teams[team] = {}

            # Loop through table columns
            for num, col in enumerate(row.find_all('td')):
                # Skipping team column
                if num != 0:
                    teams[team][header[num]] = col.get_text().replace(
                        '\n', '').replace(' ', '')

        return teams


class Offense(NFLStats):
    def passing(self):
        """Get Offensive Passing Data"""
        url = 'https://www.nfl.com/stats/team-stats/offense/passing/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def rushing(self):
        """Get Offensive Rushing Data"""
        url = 'https://www.nfl.com/stats/team-stats/offense/rushing/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def receiving(self):
        """Get Offensive Receiving Data"""
        url = 'https://www.nfl.com/stats/team-stats/offense/receiving/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def scoring(self):
        """Get Offensive Scoring Data"""
        url = 'https://www.nfl.com/stats/team-stats/offense/scoring/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def downs(self):
        """Get Offensive Downs Data"""
        url = 'https://www.nfl.com/stats/team-stats/offense/downs/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)


class Defense(NFLStats):
    def passing(self):
        """Get Defensive Passing Data"""
        url = 'https://www.nfl.com/stats/team-stats/defense/passing/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def rushing(self):
        """Get Defensive Rushing Data"""
        url = 'https://www.nfl.com/stats/team-stats/defense/rushing/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def receiving(self):
        """Get Defensive Receiving Data"""
        url = 'https://www.nfl.com/stats/team-stats/defense/receiving/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def scoring(self):
        """Get Defensive Scoring Data"""
        url = 'https://www.nfl.com/stats/team-stats/defense/scoring/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def tackles(self):
        """Get Defensive Tackles Data"""
        url = 'https://www.nfl.com/stats/team-stats/defense/tackles/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def downs(self):
        """Get Defensive Downs Data"""
        url = 'https://www.nfl.com/stats/team-stats/defense/downs/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def fumbles(self):
        """Get Defensive Fumbles Data"""
        url = 'https://www.nfl.com/stats/team-stats/defense/fumbles/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def interceptions(self):
        """Get Defensive Interceptions Data"""
        url = 'https://www.nfl.com/stats/team-stats/defense/interceptions/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)


class SpecialTeams(NFLStats):
    def field_goals(self):
        """Get Special Teams Field Goals Data"""
        url = 'https://www.nfl.com/stats/team-stats/special-teams/field-goals/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def scoring(self):
        """Get Special Teams Scoring Data"""
        url = 'https://www.nfl.com/stats/team-stats/special-teams/scoring/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def kickoffs(self):
        """Get Special Teams Kickoffs Data"""
        url = 'https://www.nfl.com/stats/team-stats/special-teams/kickoffs/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def kickoff_returns(self):
        """Get Special Teams Kickoff Returns Data"""
        url = 'https://www.nfl.com/stats/team-stats/special-teams/kickoff-returns/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def punting(self):
        """Get Special Teams Punting Data"""
        url = 'https://www.nfl.com/stats/team-stats/special-teams/punting/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)

    def punt_returns(self):
        """Get Special Teams Punt Returns Data"""
        url = 'https://www.nfl.com/stats/team-stats/special-teams/punt-returns/{}/reg/all'.format(
            self.year)

        return self._pull_stats(url)
