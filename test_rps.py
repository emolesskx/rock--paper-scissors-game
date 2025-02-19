import pytest
from unittest.mock import patch, MagicMock
from collections import defaultdict

# Import functions from the main script
from rps import ai_choice, determine_winner, save_to_mysql, save_to_firebase, player_history

@pytest.fixture(autouse=True)
def reset_player_history():
    """Reset player history before each test."""
    global player_history
    player_history = defaultdict(int)

def test_ai_choice_random():
    """Test AI's initial random choice when no history exists."""
    with patch("random.choice", return_value="Rock"):
        assert ai_choice() == "Rock"

def test_ai_choice_prediction():
    """Test AI prediction when player history is available."""
    global player_history
    player_history["Rock"] = 5  # Simulating player choosing 'Rock' most often
    assert ai_choice() == "Paper"  # AI should counter 'Rock' with 'Paper'

@pytest.mark.parametrize("player, computer, expected", [
    ("Rock", "Scissors", "You Win!"),
    ("Scissors", "Rock", "You Lose!"),
    ("Paper", "Paper", "It's a Draw!")
])
def test_determine_winner(player, computer, expected):
    """Test game logic for win, loss, and draw scenarios."""
    assert determine_winner(player, computer) == expected

@patch("your_script.connect_mysql")
def test_save_to_mysql(mock_connect):
    """Test saving to MySQL without actual database connection."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    save_to_mysql("Rock", "Paper", "You Lose!")

    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_conn.close.assert_called_once()

@patch("your_script.db.reference")
def test_save_to_firebase(mock_db_ref):
    """Test saving to Firebase without real database."""
    mock_ref = MagicMock()
    mock_db_ref.return_value = mock_ref

    save_to_firebase("Paper", "Rock", "You Win!")

    mock_ref.push.assert_called_once_with({
        "player_choice": "Paper",
        "computer_choice": "Rock",
        "result": "You Win!"
    })
