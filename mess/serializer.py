from rest_framework import serializers

from mess.models import Mess, Menu


class MessSerializer(serializers.ModelSerializer):
    """
    serialize Mess details
    """

    class Meta:
        model = Mess
        fields = "__all__"

    # def to_representation(self, data):
    #     res = super(MessSerializer, self).to_representation(data)
    #     return {res['mess_name']: res}
    # @staticmethod
    # def get_price():
    #     return Menu.objects.select_related('price')


class MenuSerializer(serializers.ModelSerializer):
    """
    serialize Menu details
    """

    address = serializers.SerializerMethodField()
    timing = serializers.SerializerMethodField()

    # menu = serializers.CharField(source='item') # change name from item to menu

    def get_address(self, obj):
        return obj.mess_id.address


    def get_timing(self, obj):
        return obj.mess_id.timing

    class Meta:
        model = Menu
        fields = ('item', 'menu_id', 'mess_id', 'address', 'timing')

