module Jekyll
    class MediaPath < Liquid::Tag
  
      def initialize(tag_name, text, tokens)
        super
        @text = text
      end
  
      def render(context)
        "{{ site.baseurl | append: 'assets/media/' | append:  page.path | replace: '.md','' | replace: '_posts/',''  }} #{@text} "
      end
    end
  end
  
  Liquid::Template.register_tag('media', Jekyll::MediaPath)