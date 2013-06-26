module VagrantPlugins
  module Fabric
    class Config < Vagrant.plugin("2", :config)
      attr_accessor :fabfile_path
      attr_accessor :fabric_path
      attr_accessor :python_path
      attr_accessor :tasks

      def initialize
        @fabfile_path = UNSET_VALUE
        @fabric_path  = UNSET_VALUE
        @python_path  = UNSET_VALUE
        @tasks        = UNSET_VALUE
      end

      def finalize!
        @fabfile_path = "fabfile.py" if @fabfile_path == UNSET_VALUE
        @fabric_path = "fab" if @fabric_path == UNSET_VALUE
        @python_path = "python" if @python_path == UNSET_VALUE
        @tasks = [] if @tasks == UNSET_VALUE
      end

      def validate(env)
        errors = _detected_errors

        if not File.exist?(fabfile_path)
          errors << "No fabfile found."
        end

        which_fabric_path = `which #{fabric_path}`
        if not $?.success?
          errors << "fabric command does not exist."
        end
        
        which_python_path = `which #{python_path}`
        if not $?.success?
          errors << "python not found."
        end

        fabfile_package = fabfile_path.gsub(".py", "").gsub("/", ".")
        output = `#{python_path} -c "exec 'import #{fabfile_package}'" &> /dev/null`
        if not $?.success?
          errors << "#{fabfile_package} could not import."
        end

        for task in tasks
          task = task.split(":")[0]
          package_path = "#{fabfile_package}.#{task}".gsub(".__init__", "")
          packages = package_path.split(".")
          output = `#{python_path} -c "exec 'from #{packages[0..-2].join('.')} import #{packages[-1]}'" > /dev/null 2>&1`
          if not $?.success?
            errors << "#{task} task does not exist."
          end
        end
        { "fabric provisioner" => errors }
      end
    end
  end
end
