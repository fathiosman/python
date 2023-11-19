import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_init(tv):
    assert tv._status is False
    assert tv._muted is False
    assert tv._volume == tv.MIN_VOLUME
    assert tv._channel == tv.MIN_CHANNEL

def test_power(tv):
    tv.power()
    assert tv._status is True

def test_mute(tv):
    tv.power()
    tv.mute()
    assert tv._muted is True

def test_unmute(tv):
    tv.power()
    tv.mute()
    tv.mute()  # unmute
    assert tv._muted is False


def test_tv_details_powered_on(tv):
    tv.power()
    assert tv.display_info() == f"Power = True, Channel = {tv._channel}, Volume = {tv._volume}"

def test_tv_details_powered_off(tv):
    assert tv.display_info() == f"Power = False, Channel = {tv._channel}, Volume = {tv._volume}"

def test_tv_details_powered_on_volume_increase_and_muted(tv):
    tv.power()
    tv.volume_up()
    tv.mute()
    assert tv.display_info() == f"Power = True, Channel = {tv._channel}, Volume = {tv._volume}"

def test_tv_details_powered_on_and_unmuted(tv):
    tv.power()
    tv.mute()
    tv.mute()  # unmute
    assert tv.display_info() == f"Power = True, Channel = {tv._channel}, Volume = {tv._volume}"

def test_tv_details_powered_off_and_muted(tv):
    tv.mute()
    assert tv.display_info() == f"Power = False, Channel = {tv._channel}, Volume = {tv._volume}"

def test_tv_details_powered_off_and_unmuted(tv):
    assert tv.display_info() == f"Power = False, Channel = {tv._channel}, Volume = {tv._volume}"

def test_channel_up(tv):
    tv.power()
    tv.channel_up()
    assert tv.display_info() == f"Power = True, Channel = {tv.MIN_CHANNEL + 1}, Volume = {tv._volume}"

def test_channel_up_past_maximum(tv):
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert tv.display_info() == f"Power = True, Channel = {tv.MIN_CHANNEL}, Volume = {tv._volume}"

def test_channel_down(tv):
    tv.power()
    tv.channel_up()  # Ensure channel is not at the minimum
    tv.channel_down()
    assert tv.display_info() == f"Power = True, Channel = {tv.MIN_CHANNEL}, Volume = {tv._volume}"

def test_channel_down_past_minimum(tv):
    tv.power()
    tv.channel_down()
    assert tv.display_info() == f"Power = True, Channel = {tv.MAX_CHANNEL}, Volume = {tv._volume}"

def test_volume_up(tv):
    tv.power()
    tv.volume_up()
    assert tv.display_info() == f"Power = True, Channel = {tv._channel}, Volume = {tv.MIN_VOLUME + 1}"

def test_volume_up_past_maximum(tv):
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert tv.display_info() == f"Power = True, Channel = {tv._channel}, Volume = {tv.MAX_VOLUME}"

def test_volume_down(tv):
    tv.power()
    tv.volume_up()  # Ensure volume is not at the minimum
    tv.volume_down()
    assert tv.display_info() == f"Power = True, Channel = {tv._channel}, Volume = {tv.MIN_VOLUME}"

def test_volume_down_past_minimum(tv):
    tv.power()
    tv.volume_down()
    assert tv.display_info() == f"Power = True, Channel = {tv._channel}, Volume = {tv.MIN_VOLUME}"

def test_volume_down_from_maximum(tv):
    tv.power()
    tv.volume_up()  # Increase volume to the maximum
    tv.volume_down()
    assert tv.display_info() == f"Power = True, Channel = {tv._channel}, Volume = {tv.MAX_VOLUME - 1}"

if __name__ == '__main__':
    pytest.main()

