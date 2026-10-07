class Page:
    """
    Screen base class
    """

    def bulid(self, parent):
        """
        Place on the parent widget
        
        return the Frame
        """

        raise NotImplementedError


    def update(self):
        """
        Update the view 
        """

        pass