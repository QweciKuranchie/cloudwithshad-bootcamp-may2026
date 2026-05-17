source "https://rubygems.org"

# GitHub Pages uses this specific Jekyll version to build sites.
# Pinning to "github-pages" gem means our local builds match GitHub's exactly.
gem "github-pages", group: :jekyll_plugins

# Theme for markdown pages
gem "minima"

# Plugins (also declared in _config.yml)
group :jekyll_plugins do
  gem "jekyll-relative-links"
end

# Windows + JRuby compatibility (mostly defensive, doesn't hurt)
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Lock http_parser to fix performance on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# webrick is needed by Jekyll 4+ but not bundled
gem "webrick", "~> 1.7"
