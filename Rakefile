require 'rake/clean'

CLEAN.include(["izon.egg-info", "dist"])

desc "Make package"
task :package do
  sh 'python setup.py sdist'
end


desc "Upload package to PyPI"
task :upload do
  sh 'twine upload dist/*'
end

task :default => [:package, :upload]
