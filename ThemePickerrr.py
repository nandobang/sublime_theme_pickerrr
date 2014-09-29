import sublime, sublime_plugin, re

class ThemePickerrrCommand(sublime_plugin.WindowCommand):
  themes = []

  def run(self):
    self.get_themes_list()
    self.window.show_quick_panel(self.themes, self.on_select_theme)

  def get_themes_list(self):
    self.themes = []
    self.themes = sublime.find_resources("*.sublime-theme")

    for i in range(len(self.themes)):
      self.themes[i] = self.prettify_theme_name(self.themes[i])

  def prettify_theme_name(self, name):
    matches = re.match('Packages/(.+)/(.+).sublime-theme', name)
    pretty_name = matches.group(2)

    return pretty_name

  def on_select_theme(self, index):
    if (index > -1):
      sublime.status_message("Changed theme to \"" + self.themes[index] + "\"")
      self.change_user_theme(self.themes[index])

  def change_user_theme(self, theme):
    s = sublime.load_settings("Preferences.sublime-settings")
    s.set("theme", theme + ".sublime-theme")