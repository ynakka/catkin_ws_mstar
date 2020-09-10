// Auto-generated. Do not edit!

// (in-package comm_thrusters.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Thrusters8 {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.FXpMZp = null;
      this.FXpMZm = null;
      this.FXmMZp = null;
      this.FXmMZm = null;
      this.FYpMZp = null;
      this.FYpMZm = null;
      this.FYmMZp = null;
      this.FYmMZm = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('FXpMZp')) {
        this.FXpMZp = initObj.FXpMZp
      }
      else {
        this.FXpMZp = 0.0;
      }
      if (initObj.hasOwnProperty('FXpMZm')) {
        this.FXpMZm = initObj.FXpMZm
      }
      else {
        this.FXpMZm = 0.0;
      }
      if (initObj.hasOwnProperty('FXmMZp')) {
        this.FXmMZp = initObj.FXmMZp
      }
      else {
        this.FXmMZp = 0.0;
      }
      if (initObj.hasOwnProperty('FXmMZm')) {
        this.FXmMZm = initObj.FXmMZm
      }
      else {
        this.FXmMZm = 0.0;
      }
      if (initObj.hasOwnProperty('FYpMZp')) {
        this.FYpMZp = initObj.FYpMZp
      }
      else {
        this.FYpMZp = 0.0;
      }
      if (initObj.hasOwnProperty('FYpMZm')) {
        this.FYpMZm = initObj.FYpMZm
      }
      else {
        this.FYpMZm = 0.0;
      }
      if (initObj.hasOwnProperty('FYmMZp')) {
        this.FYmMZp = initObj.FYmMZp
      }
      else {
        this.FYmMZp = 0.0;
      }
      if (initObj.hasOwnProperty('FYmMZm')) {
        this.FYmMZm = initObj.FYmMZm
      }
      else {
        this.FYmMZm = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Thrusters8
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [FXpMZp]
    bufferOffset = _serializer.float32(obj.FXpMZp, buffer, bufferOffset);
    // Serialize message field [FXpMZm]
    bufferOffset = _serializer.float32(obj.FXpMZm, buffer, bufferOffset);
    // Serialize message field [FXmMZp]
    bufferOffset = _serializer.float32(obj.FXmMZp, buffer, bufferOffset);
    // Serialize message field [FXmMZm]
    bufferOffset = _serializer.float32(obj.FXmMZm, buffer, bufferOffset);
    // Serialize message field [FYpMZp]
    bufferOffset = _serializer.float32(obj.FYpMZp, buffer, bufferOffset);
    // Serialize message field [FYpMZm]
    bufferOffset = _serializer.float32(obj.FYpMZm, buffer, bufferOffset);
    // Serialize message field [FYmMZp]
    bufferOffset = _serializer.float32(obj.FYmMZp, buffer, bufferOffset);
    // Serialize message field [FYmMZm]
    bufferOffset = _serializer.float32(obj.FYmMZm, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Thrusters8
    let len;
    let data = new Thrusters8(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [FXpMZp]
    data.FXpMZp = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FXpMZm]
    data.FXpMZm = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FXmMZp]
    data.FXmMZp = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FXmMZm]
    data.FXmMZm = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FYpMZp]
    data.FYpMZp = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FYpMZm]
    data.FYpMZm = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FYmMZp]
    data.FYmMZp = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [FYmMZm]
    data.FYmMZm = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'comm_thrusters/Thrusters8';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '51b0cb1b10c2fc8b58fb90e8108ac3ef';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Header header
    float32 FXpMZp
    float32 FXpMZm
    float32 FXmMZp
    float32 FXmMZm
    float32 FYpMZp
    float32 FYpMZm
    float32 FYmMZp
    float32 FYmMZm
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Thrusters8(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.FXpMZp !== undefined) {
      resolved.FXpMZp = msg.FXpMZp;
    }
    else {
      resolved.FXpMZp = 0.0
    }

    if (msg.FXpMZm !== undefined) {
      resolved.FXpMZm = msg.FXpMZm;
    }
    else {
      resolved.FXpMZm = 0.0
    }

    if (msg.FXmMZp !== undefined) {
      resolved.FXmMZp = msg.FXmMZp;
    }
    else {
      resolved.FXmMZp = 0.0
    }

    if (msg.FXmMZm !== undefined) {
      resolved.FXmMZm = msg.FXmMZm;
    }
    else {
      resolved.FXmMZm = 0.0
    }

    if (msg.FYpMZp !== undefined) {
      resolved.FYpMZp = msg.FYpMZp;
    }
    else {
      resolved.FYpMZp = 0.0
    }

    if (msg.FYpMZm !== undefined) {
      resolved.FYpMZm = msg.FYpMZm;
    }
    else {
      resolved.FYpMZm = 0.0
    }

    if (msg.FYmMZp !== undefined) {
      resolved.FYmMZp = msg.FYmMZp;
    }
    else {
      resolved.FYmMZp = 0.0
    }

    if (msg.FYmMZm !== undefined) {
      resolved.FYmMZm = msg.FYmMZm;
    }
    else {
      resolved.FYmMZm = 0.0
    }

    return resolved;
    }
};

module.exports = Thrusters8;
