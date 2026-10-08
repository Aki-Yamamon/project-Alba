from apps.clock import Clock
from apps.clock.page import ClockPage
from shell.shell import Shell

shell = Shell()
shell.add_page("clock", ClockPage(Clock()))
shell.show("clock")
shell.run()