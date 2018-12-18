class TestBasicMessageParser:
    def test_parse_complex_message(self, decoder_app, basic_parser_app):
        raw_encoding = b"8=FIX.4.4\x019=3589\x0135=W\x0134=44\x0149=market_data\x0152=20181214-14:04:51.228\x0156=J_TRADER\x0148=1000000058\x01262=0\x01263=h\x01267=1\x01269=h\x01268=168\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=11:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=12:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=13:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=14:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=15:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=16:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=17:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=18:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=19:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=20:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=21:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=22:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181213\x01273=23:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181214\x01273=01:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181214\x01273=02:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181214\x01273=03:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181214\x01273=04:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181214\x01273=05:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181214\x01273=06:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181214\x01273=07:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181214\x01273=08:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181214\x01273=09:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181214\x01273=11:00:00\x01269=4\x01270=-2147483648\x01269=7\x01270=-2147483648\x01269=8\x01270=-2147483648\x01269=5\x01270=-2147483648\x01269=B\x01270=0\x01269=v\x01270=0\x01269=s\x01272=20181214\x01273=12:00:00\x019960=1\x019961=1\x0110046=100\x0110=126\x01"
        rm = decoder_app.on_receive(
            raw_encoding
        )  # Pre-process message as would be the case in normal pipeline

        rm = basic_parser_app.on_receive(rm)
        assert rm.raw == raw_encoding
