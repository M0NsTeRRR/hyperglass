"""Constant definitions used throughout the application."""
# Standard Library Imports
import sys

MIN_PYTHON_VERSION = (3, 7)

protocol_map = {80: "http", 8080: "http", 443: "https", 8443: "https"}

target_format_space = ("huawei", "huawei_vrpv8")

LOG_FMT = (
    "<lvl><b>[{level}]</b> {time:YYYYMMDD} {time:HH:mm:ss} <lw>|</lw> {name}<lw>:</lw>"
    "<b>{line}</b> <lw>|</lw> {function}</lvl> <lvl><b>→</b></lvl> {message}"
)
LOG_LEVELS = [
    {"name": "DEBUG", "no": 10, "color": "<c>"},
    {"name": "INFO", "no": 20, "color": "<le>"},
    {"name": "SUCCESS", "no": 25, "color": "<g>"},
    {"name": "WARNING", "no": 30, "color": "<y>"},
    {"name": "ERROR", "no": 40, "color": "<y>"},
    {"name": "CRITICAL", "no": 50, "color": "<r>"},
]

LOG_HANDLER = {"sink": sys.stdout, "format": LOG_FMT, "level": "INFO"}

LOG_HANDLER_FILE = {"format": LOG_FMT, "level": "INFO"}

DEFAULT_TERMS = """
---
template: footer
---
By using {{ branding.site_name }}, you agree to be bound by the following terms of \
use: All queries executed on this page are logged for analysis and troubleshooting. \
Users are prohibited from automating queries, or attempting to process queries in \
bulk. This service is provided on a best effort basis, and {{ general.org_name }} \
makes no availability or performance warranties or guarantees whatsoever.
"""

DEFAULT_DETAILS = {
    "bgp_aspath": r"""
---
template: bgp_aspath
title: Supported AS Path Patterns
---
{{ branding.site_name }} accepts the following `AS_PATH` regular expression patterns:

| Expression           | Match                                         |
| :------------------- | :-------------------------------------------- |
| `_65000$`            | Originated by 65000                           |
| `^65000_`            | Received from 65000                           |
| `_65000_`            | Via 65000                                     |
| `_65000_65001_`      | Via 65000 and 65001                           |
| `_65000(_.+_)65001$` | Anything from 65001 that passed through 65000 |
""",
    "bgp_community": """
---
template: bgp_community
title: BGP Communities
---
{{ branding.site_name }} makes use of the following BGP communities:

| Community | Description |
| :-------- | :---------- |
| `65000:1` | Example 1   |
| `65000:2` | Example 2   |
| `65000:3` | Example 3   |
""",
}

DEFAULT_INFO = {
    "bgp_route": """
---
template: bgp_route
---
Performs BGP table lookup based on IPv4/IPv6 prefix.
""",
    "bgp_community": """
---
template: bgp_community
---
Performs BGP table lookup based on <a href="https://tools.ietf.org/html/rfc4360" target\
="_blank">Extended</a> or <a href="https://tools.ietf.org/html/rfc8195" target=\
"_blank">Large</a> community value.

""",
    "bgp_aspath": """
---
template: bgp_aspath
---
Performs BGP table lookup based on `AS_PATH` regular expression.

""",
    "ping": """
---
template: ping
---
Sends 5 ICMP echo requests to the target.
""",
    "traceroute": """
---
template: traceroute
---
Performs UDP Based traceroute to the target.<br>For information about how to \
interpret traceroute results, <a href="https://hyperglass.readthedocs.io/en/latest/ass\
ets/traceroute_nanog.pdf" target="_blank">click here</a>.
""",
}


DEFAULT_HELP = """
---
template: default_help
---
##### BGP Route
Performs BGP table lookup based on IPv4/IPv6 prefix.
<hr>
##### BGP Community
Performs BGP table lookup based on <a href="https://tools.ietf.org/html/rfc4360" target\
="_blank">Extended</a> or <a href="https://tools.ietf.org/html/rfc8195" target=\
"_blank">Large</a> community value.
<hr>
##### BGP AS Path
Performs BGP table lookup based on `AS_PATH` regular expression.
<hr>
##### Ping
Sends 5 ICMP echo requests to the target.
<hr>
##### Traceroute
Performs UDP Based traceroute to the target.<br>For information about how to \
interpret traceroute results, <a href="https://hyperglass.readthedocs.io/en/latest/ass\
ets/traceroute_nanog.pdf" target="_blank">click here</a>.
"""


class Supported:
    """Define items supported by hyperglass.

    query_types: Supported query types used to validate Flask input.

    rest: Supported REST API platforms

    scrape: Supported "scrape" platforms which will be accessed via
    Netmiko. List updated 07/2019.
    """

    query_parameters = ("query_location", "query_type", "query_target", "query_vrf")

    query_types = ("bgp_route", "bgp_community", "bgp_aspath", "ping", "traceroute")

    rest = ("frr", "bird")

    scrape = (
        "a10",
        "accedian",
        "alcatel_aos",
        "alcatel_sros",
        "apresia_aeos",
        "arista_eos",
        "aruba_os",
        "avaya_ers",
        "avaya_vsp",
        "brocade_fastiron",
        "brocade_netiron",
        "brocade_nos",
        "brocade_vdx",
        "brocade_vyos",
        "checkpoint_gaia",
        "calix_b6",
        "ciena_saos",
        "cisco_asa",
        "cisco_ios",
        "cisco_ios_telnet",
        "cisco_nxos",
        "cisco_s300",
        "cisco_tp",
        "cisco_wlc",
        "cisco_xe",
        "cisco_xr",
        "coriant",
        "dell_dnos9",
        "dell_force10",
        "dell_os6",
        "dell_os9",
        "dell_os10",
        "dell_powerconnect",
        "dell_isilon",
        "eltex",
        "enterasys",
        "extreme",
        "extreme_ers",
        "extreme_exos",
        "extreme_netiron",
        "extreme_nos",
        "extreme_slx",
        "extreme_vdx",
        "extreme_vsp",
        "extreme_wing",
        "f5_ltm",
        "f5_tmsh",
        "f5_linux",
        "fortinet",
        "generic_termserver",
        "hp_comware",
        "hp_procurve",
        "huawei",
        "huawei_vrpv8",
        "ipinfusion_ocnos",
        "juniper",
        "juniper_junos",
        "linux",
        "mellanox",
        "mrv_optiswitch",
        "netapp_cdot",
        "netscaler",
        "ovs_linux",
        "paloalto_panos",
        "pluribus",
        "quanta_mesh",
        "rad_etx",
        "ruckus_fastiron",
        "ubiquiti_edge",
        "ubiquiti_edgeswitch",
        "vyatta_vyos",
        "vyos",
        "oneaccess_oneos",
    )

    @staticmethod
    def is_supported(nos):
        """Verify if NOS is supported.

        Arguments:
            nos {str} -- NOS short name

        Returns:
            {bool} -- True if supported
        """
        return bool(nos in Supported.rest + Supported.scrape)

    @staticmethod
    def is_scrape(nos):
        """Verify if NOS transport is scrape.

        Arguments:
            nos {str} -- NOS short name

        Returns:
            {bool} -- True if scrape
        """
        return bool(nos in Supported.scrape)

    @staticmethod
    def is_rest(nos):
        """Verify if NOS transport is REST.

        Arguments:
            nos {str} -- NOS short name

        Returns:
            {bool} -- True if REST
        """
        return bool(nos in Supported.rest)

    @staticmethod
    def is_supported_query(query_type):
        """Verify if query type is supported.

        Arguments:
            query_type {str} -- query type

        Returns:
            {bool} -- True if supported
        """
        return bool(query_type in Supported.query_types)

    @staticmethod
    def map_transport(nos):
        """Map NOS to transport name.

        Arguments:
            nos {str} -- NOS short name

        Returns:
            {str} -- Transport name
        """
        transport = None
        if nos in Supported.scrape:
            transport = "scrape"
        elif nos in Supported.rest:
            transport = "rest"
        return transport
