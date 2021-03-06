# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ublox_msgs/CfgGNSS.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ublox_msgs.msg

class CfgGNSS(genpy.Message):
  _md5sum = "c1777482e22a0ac50132c66d3284e86f"
  _type = "ublox_msgs/CfgGNSS"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# CFG-GNSS (0x06 0x3E)
# GNSS Configuration
#
# Gets or sets the GNSS system channel sharing configuration.
# If the receiver is sent a valid new configuration, it will respond with a 
# UBX-ACK-ACK message and immediately change to the new configuration. Otherwise
# the receiver will reject the request, by issuing a UBX-ACK-NAK and continuing 
# operation with the previous configuration.
# Configuration requirements:
#  - It is necessary for at least one major GNSS to be enabled, after applying 
#    the new configuration to the current one.
#  - It is also required that at least 4 tracking channels are available to each 
#    enabled major GNSS, i.e. maxTrkCh must have a minimum value of 4 for each
#    enabled major GNSS.
#  - The number of tracking channels in use must not exceed the number of 
#    tracking channels available in hardware, and the sum of all reserved 
#    tracking channels needs to be less than or equal to the number of tracking
#    channels in use.
# Notes:
#  - To avoid cross-correlation issues, it is recommended that GPS and QZSS are
#    always both enabled or both disabled.
#  - Polling this message returns the configuration of all supported GNSS, 
#    whether enabled or not; it may also include GNSS unsupported by the 
#    particular product, but in such cases the enable flag will always be unset.
#  - See section GNSS Configuration for a discussion of the use of this message 
#    and section Satellite Numbering for a description of the GNSS IDs available
#  - Configuration specific to the GNSS system can be done via other messages 
#    (e.g. UBX-CFG-SBAS).
#

uint8 CLASS_ID = 6
uint8 MESSAGE_ID = 62

uint8 msgVer            # Message version (= 0 for this version)
uint8 numTrkChHw        # Number of tracking channels in hardware (read only)
uint8 numTrkChUse       # (Read only in protocol versions greater than 23)
                        # Number of tracking channels to use (<= numTrkChHw)
                        # If 0xFF, then number of tracking channels to use will 
                        # be set to numTrkChHw
uint8 numConfigBlocks   # Number of configuration blocks following

# Start of repeated block (numConfigBlocks times)
CfgGNSS_Block[] blocks
# End of repeated block
================================================================================
MSG: ublox_msgs/CfgGNSS_Block
# see Cfg-GNSS message
#

uint8 gnssId            # System identifier (see Satellite Numbering)

uint8 GNSS_ID_GPS = 0
uint8 GNSS_ID_SBAS = 1
uint8 GNSS_ID_GALILEO = 2
uint8 GNSS_ID_BEIDOU = 3
uint8 GNSS_ID_IMES = 4
uint8 GNSS_ID_QZSS = 5
uint8 GNSS_ID_GLONASS = 6

uint8 resTrkCh          # (Read only in protocol versions greater than 23)
                        # Number of reserved (minimum) tracking channels 
                        # for this GNSS system
uint8 RES_TRK_CH_GPS = 8
uint8 RES_TRK_CH_QZSS = 0
uint8 RES_TRK_CH_SBAS = 0
uint8 RES_TRK_CH_GLONASS = 8
uint8 maxTrkCh          # (Read only in protocol versions greater than 23)
                        # Maximum number of tracking channels used for this 
                        # system. Must be > 0, >= resTrkChn, <= numTrkChUse and
                        # <= maximum number of tracking channels supported for 
                        # this system
uint8 MAX_TRK_CH_MAJOR_MIN = 4         # maxTrkCh must have this minimum value
                                       # for each enabled major GNSS
uint8 MAX_TRK_CH_GPS = 16
uint8 MAX_TRK_CH_GLONASS = 14
uint8 MAX_TRK_CH_QZSS = 3
uint8 MAX_TRK_CH_SBAS = 3

uint8 reserved1         # Reserved

uint32 flags            # Bitfield of flags. At least one signal must be
                        # configured in every enabled system. 
uint32 FLAGS_ENABLE = 1                # Enable this system
uint32 FLAGS_SIG_CFG_MASK = 16711680   # Signal configuration mask
uint32 SIG_CFG_GPS_L1CA = 65536        # When gnssId is 0 (GPS)
                                       # * 0x01 = GPS L1C/A
uint32 SIG_CFG_SBAS_L1CA = 65536       # When gnssId is 1 (SBAS)
                                       # * 0x01 = SBAS L1C/A
uint32 SIG_CFG_GALILEO_E1OS = 65536    # When gnssId is 2 (Galileo)
                                       # * 0x01 = Galileo E1OS (not supported in 
                                       #   protocol versions less than 18)
uint32 SIG_CFG_BEIDOU_B1I = 65536      # When gnssId is 3 (BeiDou)
                                       # * 0x01 = BeiDou B1I 
uint32 SIG_CFG_IMES_L1 = 65536         # When gnssId is 4 (IMES)
                                       # * 0x01 = IMES L1
uint32 SIG_CFG_QZSS_L1CA = 65536       # When gnssId is 5 (QZSS)
                                       # * 0x01 = QZSS L1C/A
uint32 SIG_CFG_QZSS_L1SAIF = 262144    # * 0x04 = QZSS L1SAIF
uint32 SIG_CFG_GLONASS_L1OF = 65536    # When gnssId is 6 (GLONASS)
                                       # * 0x01 = GLONASS L1OF"""
  # Pseudo-constants
  CLASS_ID = 6
  MESSAGE_ID = 62

  __slots__ = ['msgVer','numTrkChHw','numTrkChUse','numConfigBlocks','blocks']
  _slot_types = ['uint8','uint8','uint8','uint8','ublox_msgs/CfgGNSS_Block[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       msgVer,numTrkChHw,numTrkChUse,numConfigBlocks,blocks

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CfgGNSS, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.msgVer is None:
        self.msgVer = 0
      if self.numTrkChHw is None:
        self.numTrkChHw = 0
      if self.numTrkChUse is None:
        self.numTrkChUse = 0
      if self.numConfigBlocks is None:
        self.numConfigBlocks = 0
      if self.blocks is None:
        self.blocks = []
    else:
      self.msgVer = 0
      self.numTrkChHw = 0
      self.numTrkChUse = 0
      self.numConfigBlocks = 0
      self.blocks = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4B().pack(_x.msgVer, _x.numTrkChHw, _x.numTrkChUse, _x.numConfigBlocks))
      length = len(self.blocks)
      buff.write(_struct_I.pack(length))
      for val1 in self.blocks:
        _x = val1
        buff.write(_get_struct_4BI().pack(_x.gnssId, _x.resTrkCh, _x.maxTrkCh, _x.reserved1, _x.flags))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.blocks is None:
        self.blocks = None
      end = 0
      _x = self
      start = end
      end += 4
      (_x.msgVer, _x.numTrkChHw, _x.numTrkChUse, _x.numConfigBlocks,) = _get_struct_4B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.blocks = []
      for i in range(0, length):
        val1 = ublox_msgs.msg.CfgGNSS_Block()
        _x = val1
        start = end
        end += 8
        (_x.gnssId, _x.resTrkCh, _x.maxTrkCh, _x.reserved1, _x.flags,) = _get_struct_4BI().unpack(str[start:end])
        self.blocks.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4B().pack(_x.msgVer, _x.numTrkChHw, _x.numTrkChUse, _x.numConfigBlocks))
      length = len(self.blocks)
      buff.write(_struct_I.pack(length))
      for val1 in self.blocks:
        _x = val1
        buff.write(_get_struct_4BI().pack(_x.gnssId, _x.resTrkCh, _x.maxTrkCh, _x.reserved1, _x.flags))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.blocks is None:
        self.blocks = None
      end = 0
      _x = self
      start = end
      end += 4
      (_x.msgVer, _x.numTrkChHw, _x.numTrkChUse, _x.numConfigBlocks,) = _get_struct_4B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.blocks = []
      for i in range(0, length):
        val1 = ublox_msgs.msg.CfgGNSS_Block()
        _x = val1
        start = end
        end += 8
        (_x.gnssId, _x.resTrkCh, _x.maxTrkCh, _x.reserved1, _x.flags,) = _get_struct_4BI().unpack(str[start:end])
        self.blocks.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4B = None
def _get_struct_4B():
    global _struct_4B
    if _struct_4B is None:
        _struct_4B = struct.Struct("<4B")
    return _struct_4B
_struct_4BI = None
def _get_struct_4BI():
    global _struct_4BI
    if _struct_4BI is None:
        _struct_4BI = struct.Struct("<4BI")
    return _struct_4BI
