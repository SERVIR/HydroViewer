from tethys_sdk.base import TethysAppBase, url_map_maker


class Hydroviewer(TethysAppBase):
    """
    Tethys app class for HydroViewer.
    """

    name = 'HydroViewer'
    index = 'hydroviewer:home'
    icon = 'hydroviewer/images/logo.png'
    package = 'hydroviewer'
    root_url = 'hydroviewer'
    color = '#2980b9'
    description = 'Place a brief description of your app here.'
    tags = 'Hydrology'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='hydroviewer',
                controller='hydroviewer.controllers.home'),
            UrlMap(
                name='get-available-dates',
                url='hydroviewer/ecmwf-rapid/get-available-dates',
                controller='hydroviewer.controllers.get_available_dates'),
            UrlMap(name='get-time-series',
                   url='hydroviewer/ecmwf-rapid/get-time-series',
                   controller='hydroviewer.controllers.ecmwf_get_time_series'),
            UrlMap(name='get-return-periods',
                   url='hydroviewer/ecmwf-rapid/get-return-periods',
                   controller='hydroviewer.controllers.get_return_periods'),
        )

        return url_maps
