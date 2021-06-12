class Jekyll::Converters::Markdown::CustomProcessor

    def initialize(config)

    end

    def matches(ext)
        ext =~ /^\.(md|markdown)$/i
    end

    def output_ext(ext)
        ".html"
    end

    def convert(content)

      puts "EXECUTED"

      md_path = "./_plugins/temp/temp.md"
      html_path = "./_plugins/temp/temp.html"
      
      File.write(md_path, content, mode: "w")
      system("python ./_plugins/MyConverter.py")

      content = File.read(html_path)
      content
    end
end