# coding: utf-8

Gem::Specification.new do |spec|
  spec.name          = "ed."
  spec.version       = "1.0.2"
  spec.authors       = ["Alex Gil"]
  spec.email         = ["colibri.alex@gmail.com"]

  spec.summary       = "A Jekyll theme for minimal editions"
  spec.homepage      = "http://minicomp.github.io/ed/"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r{^(assets|optional|_layouts|_includes|_sass|_texts|index|search|about|credits|documentation|atom|Gemfile|LICENSE|README)}i) }

  spec.add_runtime_dependency "jekyll", "~> 3.6"

  spec.add_development_dependency "bundler", "~> 2.2.33" # 1.16" #hp laptop use 2.1.4 / asus laptop use 1.16 (situation as of 2 April 2020)
  spec.add_development_dependency "rake", "~> 12.3.3" #10.4"
end
