from HTMLParser import HTMLParser


class Profoundprogrammer(HTMLParser):
    hd_image = []
    images = []
    hd_image_detected = False

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                (attr_name, attr_value) = attr
                if (attr_name == 'href' and self.hd_image_detected == True):
                    print 'img attr: %s' % attr_value
                    self.images.append(attr_value)

        #print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        if 'HD' in data:
            self.hd_image_detected = True
            print 'HD image: %s' % self.images[len(self.images) - 1:]

        else:
            #self.remove_link()
            pass
