import pytest
from string_utils import StringUtils

# Создаем экземпляр один раз для всех тестов (можно также делать в setUp, но так проще для старта)
utils = StringUtils()


class TestStringUtils:
    """Тесты для класса StringUtils"""

    # --- capitalize ---
    def test_capitalize_normal(self):
        assert utils.capitalize("skypro") == "Skypro"

    def test_capitalize_all_upper(self):
        assert utils.capitalize("SKYPRO") == "Skypro"

    def test_capitalize_empty(self):
        assert utils.capitalize("") == ""

    def test_capitalize_space_start(self):
        assert utils.capitalize(" skypro") == " skypro"

    def test_capitalize_none_raises(self):
        # Ожидаем AttributeError, так как в оригинальном коде нет проверки на None
        with pytest.raises(AttributeError):
            utils.capitalize(None)

    # --- trim ---
    def test_trim_normal_leading_spaces(self):
        assert utils.trim("   skypro") == "skypro"

    def test_trim_no_leading_spaces(self):
        assert utils.trim("skypro") == "skypro"

    def test_trim_empty(self):
        assert utils.trim("") == ""

    def test_trim_only_spaces(self):
        assert utils.trim("    ") == ""

    def test_trim_tab_not_removed(self):
        # Тест на дефект: оригинальный trim не удаляет табуляцию
        assert utils.trim("\t\tskypro") != "skypro"
        assert utils.trim("\t\tskypro") == "\t\tskypro"

    def test_trim_none_raises(self):
        with pytest.raises(AttributeError):
            utils.trim(None)

    # --- contains ---
    def test_contains_true_single_char(self):
        assert utils.contains("SkyPro", "S") is True

    def test_contains_false(self):
        assert utils.contains("SkyPro", "U") is False

    def test_contains_empty_string(self):
        assert utils.contains("", "a") is False

    def test_contains_symbol_as_substring(self):
        assert utils.contains("SkyPro", "Pro") is True

    def test_contains_none_string_raises(self):
        with pytest.raises(AttributeError):
            utils.contains(None, "a")

    def test_contains_none_symbol_raises(self):
        with pytest.raises(TypeError):
            utils.contains("SkyPro", None)

    # --- delete_symbol ---
    def test_delete_symbol_single_char(self):
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_substring(self):
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_not_found(self):
        assert utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_delete_symbol_empty_string(self):
        assert utils.delete_symbol("", "a") == ""

    def test_delete_symbol_remove_all_occurrences(self):
        assert utils.delete_symbol("aaaa", "a") == ""

    def test_delete_symbol_none_string_raises(self):
        with pytest.raises(AttributeError):
            utils.delete_symbol(None, "a")

    def test_delete_symbol_none_symbol_raises(self):
        with pytest.raises(TypeError):
            utils.delete_symbol("SkyPro", None)
