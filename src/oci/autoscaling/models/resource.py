# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Resource(object):
    """
    A resource that is managed by an autoscaling configuration. The only supported type is \"instancePool.\"

    Each instance pool can have one autoscaling configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Resource object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.autoscaling.models.InstancePoolResource`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Resource.
        :type type: str

        :param id:
            The value to assign to the id property of this Resource.
        :type id: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id'
        }

        self._type = None
        self._id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'instancePool':
            return 'InstancePoolResource'
        else:
            return 'Resource'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Resource.
        The type of resource.


        :return: The type of this Resource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Resource.
        The type of resource.


        :param type: The type of this Resource.
        :type: str
        """
        self._type = type

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Resource.
        The `OCID`__ of the resource that is managed by the autoscaling configuration.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Resource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Resource.
        The `OCID`__ of the resource that is managed by the autoscaling configuration.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Resource.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
