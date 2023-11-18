#codex #dreambot 

``` Java
import org.dreambot.api.methods.Calculations;
import org.dreambot.api.methods.container.impl.bank.BankLocation;
import org.dreambot.api.methods.container.impl.equipment.EquipmentSlot;
import org.dreambot.api.methods.filter.Filter;
import org.dreambot.api.methods.map.Area;
import org.dreambot.api.methods.map.Tile;
import org.dreambot.api.methods.skills.Skill;
import org.dreambot.api.methods.tabs.Tab;
import org.dreambot.api.methods.walking.path.impl.LocalPath;
import org.dreambot.api.methods.walking.path.impl.WalkingPath;
import org.dreambot.api.methods.widget.Widget;
import org.dreambot.api.methods.world.World;
import org.dreambot.api.script.AbstractScript;
import org.dreambot.api.script.Category;
import org.dreambot.api.script.ScriptManifest;
import org.dreambot.api.wrappers.interactive.GameObject;
import org.dreambot.api.wrappers.interactive.NPC;
import org.dreambot.api.wrappers.items.GroundItem;
import org.dreambot.api.wrappers.items.Item;
import org.dreambot.api.wrappers.widgets.WidgetChild;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

@ScriptManifest(author = "Dylan", category = Category.COMBAT, description = "Kills Hill Giants", name = "Dylans Hill Giant Killer", version = 1.0)
public class Main extends AbstractScript {

    private final Area hillGiantArea = new Area(3111, 9850, 3120, 9840);
    private final Area bankArea = new Area(3093, 3491, 3097, 3487);
    private final Area pathToBank = new Area(3111, 9850, 3120, 9840);
    private final Area pathToHillGiants = new Area(3093, 3491, 3097, 3487);
     private final Filter<NPC> hillGiantFilter = new Filter<NPC>() {
        @Override
        public boolean match(NPC npc) {
            return npc != null && npc.getName().equals("Hill Giant") && npc.getHealthPercent() > 0;
        }
    };

    private final Filter<GroundItem> foodFilter = new Filter<GroundItem>() {
        @Override
        public boolean match(GroundItem groundItem) {
            return groundItem != null && groundItem.getName().equals("Lobster") && groundItem.distance() < 10;
        }
    };

    private final Filter<GameObject> doorFilter = new Filter<GameObject>() {
        @Override
        public boolean match(GameObject gameObject) {
            return gameObject != null && gameObject.getName().equals("Door") && gameObject.distance() < 10;
        }
    };

    private final Filter<Item> foodInInventoryFilter = new Filter<Item>() {
        @Override
        public boolean match(Item item) {
            return item != null && item.getName().equals("Lobster") && item.getAmount() > 0;
        }
    };

    private final Filter<Item> foodInBankFilter = new Filter<Item>() {
        @Override
        public boolean match(Item item) {
            return item != null && item.getName().equals("Lobster") && item.getAmount() > 0;
        }
    };

    private final Filter<Item> foodInEquipmentFilter = new Filter<Item>() {
        @Override
        public boolean match(Item item) {
            return item != null && item.getName().equals("Lobster") && item.getAmount() > 0;
        }
    };

```
