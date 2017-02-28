class SipRouter(object):
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == 'sip_oracle':
            return 'sip_oracle'
        return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     """
    #     Allow relations if a model in the auth app is involved.
    #     """
    #     if obj1._meta.app_label == 'sip_oracle' or \
    #             obj2._meta.app_label == 'sip_oracle':
    #         return True
    #     return None
