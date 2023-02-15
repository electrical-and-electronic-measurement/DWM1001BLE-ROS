#!/usr/bin/env python

Devices = [
    {
        "Name": "Celeste",
        "MAC": "C9:3D:ED:68:62:DD",
        "InitialStatus": "Tag",
        "nodeIndex": 1,
        "HasTwoDevice": False,
        "OptitrackStreamingId": 3,

    },
    {
        "Name": "Fucsia",
        "MAC": "E4:DD:A3:32:F9:0A",
        "InitialStatus": "Tag",
        "nodeIndex": 3,
        "HasTwoDevice": False,

    },
    {
        "Name": "Viola",
        "MAC": "C2:98:EF:BF:22:37",
        "InitialStatus": "Tag",
        "nodeIndex": 2,
        "HasTwoDevice": False,

    },
    {
        "Name": "Verde",
        "MAC": "C8:2D:9F:F6:18:BA",
        "InitialStatus": "Anchor",
        "nodeId": 21760,
        "HasTwoDevice": False,
        "nodeIndex": 0,

    },
    {
        "Name": "Senape",
        "MAC": "F2:73:A8:0C:A4:88",
        "InitialStatus": "Anchor",
        "nodeId": 54288,
        "nodeIndex": 1,
        # this has to be true only in one of the two item with same nodeIndex
        "HasTwoDevice": True,
    }
]


# topics name
BLEDecawaveRangingTopicName = "/Decawave_Ranging_Topic"
